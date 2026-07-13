from app.paper_trading_v1.domain.models import PaperDashboard, PaperTradingState

class PaperDashboardEngineV1:
    def build(self, state: PaperTradingState) -> PaperDashboard:
        exposure = sum(abs(p.mark_price * p.quantity) for p in state.positions if p.status == "open")
        return PaperDashboard(
            equity=state.account.equity,
            cash=state.account.cash,
            realized_pnl=state.account.realized_pnl,
            unrealized_pnl=state.account.unrealized_pnl,
            open_positions=sum(1 for p in state.positions if p.status == "open"),
            total_orders=len(state.orders),
            fees_paid=state.account.fees_paid,
            exposure=exposure,
            journal_count=len(state.journal),
        )
