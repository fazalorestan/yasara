from app.decision_v1.domain.models import DecisionDirection
from app.portfolio_v1.domain.models import ExposureItem, ExposureMatrix, PortfolioSnapshot, PositionStatus

class ExposureEngineV1:
    def calculate(self, snapshot: PortfolioSnapshot) -> ExposureMatrix:
        open_positions = [p for p in snapshot.positions if p.status == PositionStatus.OPEN]
        total = sum(p.notional for p in open_positions)
        long_exposure = sum(p.notional for p in open_positions if p.direction == DecisionDirection.LONG)
        short_exposure = sum(p.notional for p in open_positions if p.direction == DecisionDirection.SHORT)
        items = [
            ExposureItem(
                symbol=p.symbol,
                notional=p.notional,
                exposure_pct=(p.notional / snapshot.equity * 100) if snapshot.equity else 0,
                direction=p.direction,
                pnl=p.unrealized_pnl,
            )
            for p in open_positions
        ]
        return ExposureMatrix(
            total_exposure=total,
            total_exposure_pct=(total / snapshot.equity * 100) if snapshot.equity else 0,
            long_exposure=long_exposure,
            short_exposure=short_exposure,
            net_exposure=long_exposure - short_exposure,
            items=items,
        )
