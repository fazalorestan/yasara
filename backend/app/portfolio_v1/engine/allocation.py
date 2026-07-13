from app.portfolio_v1.domain.models import AllocationItem, AllocationReport, ExposureMatrix

class AllocationEngineV1:
    def calculate(self, exposure: ExposureMatrix, targets: dict[str, float] | None = None) -> AllocationReport:
        targets = targets or self._equal_targets([i.symbol for i in exposure.items])
        items = []
        for item in exposure.items:
            target = targets.get(item.symbol, 0)
            delta = item.exposure_pct - target
            items.append(AllocationItem(symbol=item.symbol, current_pct=item.exposure_pct, target_pct=target, rebalance_required=abs(delta) >= 5, delta_pct=delta))
        concentration = max((i.current_pct for i in items), default=0)
        return AllocationReport(items=items, concentration_score=concentration, diversification_score=max(0, 100-concentration))

    def _equal_targets(self, symbols: list[str]) -> dict[str, float]:
        if not symbols: return {}
        target = 100 / len(symbols)
        return {symbol: target for symbol in symbols}
