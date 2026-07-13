import uuid
from datetime import datetime, timezone
from app.decision_v1.domain.models import DecisionDirection
from app.paper_trading_v1.domain.models import (
    PaperAccount,
    PaperExecutionReport,
    PaperOrder,
    PaperOrderRequest,
    PaperOrderSide,
    PaperOrderStatus,
    PaperTradingState,
)
from app.paper_trading_v1.engine.journal import PaperJournalEngineV1
from app.paper_trading_v1.engine.position_manager import PaperPositionManagerV1
from app.paper_trading_v1.engine.pricing import PaperPricingEngineV1

class PaperOrderManagerV1:
    def __init__(self, fee_rate: float = 0.0004):
        self.fee_rate = fee_rate
        self.pricing = PaperPricingEngineV1()
        self.positions = PaperPositionManagerV1()
        self.journal = PaperJournalEngineV1()

    def execute_market_order(self, state: PaperTradingState, request: PaperOrderRequest, market_price: float) -> PaperExecutionReport:
        if request.quantity <= 0:
            order = self._rejected(request, "Quantity must be positive.")
            state.orders.append(order)
            return PaperExecutionReport(accepted=False, order=order, message=order.rejection_reason, state=state)

        fill = self.pricing.fill_price(request, market_price)
        notional = fill * request.quantity
        fee = abs(notional) * self.fee_rate

        if request.side == PaperOrderSide.BUY and state.account.cash < notional + fee:
            order = self._rejected(request, "Insufficient paper cash.")
            state.orders.append(order)
            return PaperExecutionReport(accepted=False, order=order, message=order.rejection_reason, state=state)

        order = PaperOrder(
            order_id=uuid.uuid4().hex,
            request=request,
            status=PaperOrderStatus.FILLED,
            filled_quantity=request.quantity,
            average_fill_price=fill,
            fee=fee,
            filled_at=datetime.now(timezone.utc),
        )
        direction = DecisionDirection.LONG if request.side == PaperOrderSide.BUY else DecisionDirection.SHORT
        position = self.positions.open_position(
            symbol=request.symbol,
            direction=direction,
            quantity=request.quantity,
            fill_price=fill,
            stop_loss=request.stop_loss,
            take_profit=request.take_profit,
        )

        if request.side == PaperOrderSide.BUY:
            state.account.cash -= notional + fee
        else:
            state.account.cash -= fee

        state.account.fees_paid += fee
        state.orders.append(order)
        state.positions.append(position)
        state.journal.append(self.journal.entry(state.account.account_id, request.symbol, "open_position", "Paper position opened.", metadata={"order_id": order.order_id}))
        self._recalculate_account(state)
        return PaperExecutionReport(accepted=True, order=order, position=position, message="Paper order filled.", state=state)

    def mark_to_market(self, state: PaperTradingState, prices: dict[str, float]) -> PaperTradingState:
        for position in state.positions:
            if position.status != "open":
                continue
            price = prices.get(position.symbol)
            if price is None:
                continue
            should_close, reason = self.positions.should_close(position, price)
            if should_close:
                self.positions.close_position(position, price, reason)
                state.account.realized_pnl += position.realized_pnl
                state.journal.append(self.journal.entry(state.account.account_id, position.symbol, "close_position", f"Position closed by {reason}.", pnl=position.realized_pnl))
            else:
                self.positions.update_mark(position, price)
        self._recalculate_account(state)
        return state

    def _recalculate_account(self, state: PaperTradingState) -> None:
        state.account.unrealized_pnl = sum(p.unrealized_pnl for p in state.positions if p.status == "open")
        state.account.equity = state.account.cash + state.account.realized_pnl + state.account.unrealized_pnl

    def _rejected(self, request: PaperOrderRequest, reason: str) -> PaperOrder:
        return PaperOrder(order_id=uuid.uuid4().hex, request=request, status=PaperOrderStatus.REJECTED, rejection_reason=reason)
