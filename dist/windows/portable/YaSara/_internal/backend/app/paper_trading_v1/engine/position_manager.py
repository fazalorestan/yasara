import uuid
from app.decision_v1.domain.models import DecisionDirection
from app.paper_trading_v1.domain.models import PaperPosition, PaperPositionStatus

class PaperPositionManagerV1:
    def open_position(self, symbol: str, direction: DecisionDirection, quantity: float, fill_price: float, stop_loss: float | None, take_profit: float | None) -> PaperPosition:
        return PaperPosition(
            position_id=uuid.uuid4().hex,
            symbol=symbol,
            direction=direction,
            quantity=quantity,
            entry_price=fill_price,
            mark_price=fill_price,
            stop_loss=stop_loss,
            take_profit=take_profit,
        )

    def update_mark(self, position: PaperPosition, mark_price: float) -> PaperPosition:
        position.mark_price = mark_price
        if position.direction == DecisionDirection.LONG:
            position.unrealized_pnl = (mark_price - position.entry_price) * position.quantity
        elif position.direction == DecisionDirection.SHORT:
            position.unrealized_pnl = (position.entry_price - mark_price) * position.quantity
        return position

    def close_position(self, position: PaperPosition, exit_price: float, reason: str) -> PaperPosition:
        position = self.update_mark(position, exit_price)
        position.realized_pnl = position.unrealized_pnl
        position.unrealized_pnl = 0
        position.status = PaperPositionStatus.CLOSED
        position.exit_price = exit_price
        position.exit_reason = reason
        from datetime import datetime, timezone
        position.closed_at = datetime.now(timezone.utc)
        return position

    def should_close(self, position: PaperPosition, mark_price: float) -> tuple[bool, str]:
        if position.direction == DecisionDirection.LONG:
            if position.stop_loss is not None and mark_price <= position.stop_loss:
                return True, "stop_loss"
            if position.take_profit is not None and mark_price >= position.take_profit:
                return True, "take_profit"
        if position.direction == DecisionDirection.SHORT:
            if position.stop_loss is not None and mark_price >= position.stop_loss:
                return True, "stop_loss"
            if position.take_profit is not None and mark_price <= position.take_profit:
                return True, "take_profit"
        return False, ""
