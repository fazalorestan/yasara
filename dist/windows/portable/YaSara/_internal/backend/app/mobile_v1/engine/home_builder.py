from app.dashboard_v1.application.service import dashboard_service_v1
from app.mobile_v1.domain.models import (
    MobileHomePayload,
    MobilePortfolioSummary,
    MobileSignalCard,
    MobileWatchlistCard,
    MobileRiskCard,
)

class MobileHomeBuilderV1:
    async def build(self, owner_id: str = "default") -> MobileHomePayload:
        snapshot = await dashboard_service_v1.snapshot()
        portfolio_panel = next((p for p in snapshot.panels if p.panel_id == "portfolio"), None)
        risk_panel = next((p for p in snapshot.panels if p.panel_id == "risk"), None)

        portfolio_values = {m.key: m.value for m in portfolio_panel.metrics} if portfolio_panel else {}
        risk_values = {m.key: m.value for m in risk_panel.metrics} if risk_panel else {}

        portfolio = MobilePortfolioSummary(
            equity=float(portfolio_values.get("equity", 10000)),
            cash=float(portfolio_values.get("equity", 10000)),
            exposure=float(portfolio_values.get("exposure", 0)),
            realized_pnl=float(portfolio_values.get("pnl", 0)),
            unrealized_pnl=0,
            open_positions=0,
        )

        watchlist = [
            MobileWatchlistCard(
                symbol=item.symbol,
                price=item.price,
                change_percent=item.change_percent,
                confidence=item.confidence,
            )
            for item in snapshot.watchlist
        ]

        signals = [
            MobileSignalCard(
                symbol=s.symbol,
                direction=s.direction,
                confidence=s.confidence,
                quality_score=s.quality,
                title=f"{s.symbol} {s.direction.upper()}",
                summary=s.reason,
            )
            for s in snapshot.signals
        ]

        risk_score = float(risk_values.get("risk_score", 0))
        risk = MobileRiskCard(
            risk_score=risk_score,
            risk_level="high" if risk_score >= 70 else "medium" if risk_score >= 35 else "low",
        )

        return MobileHomePayload(
            owner_id=owner_id,
            portfolio=portfolio,
            watchlist=watchlist,
            signals=signals,
            risk=risk,
        )
