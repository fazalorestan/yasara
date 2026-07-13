from app.v11_ai_market_intelligence.models import MarketFeatureVectorV11
from app.v11_market_data.models import MarketSnapshotItemV11


class MarketFeatureBuilderV11:
    def from_snapshot_item(self, item: MarketSnapshotItemV11) -> MarketFeatureVectorV11:
        spread = item.spread or 0.0
        last = item.last_price or 0.0
        spread_ratio = (spread / last) if last else 0.0
        volatility_score = min(max(spread_ratio * 1000, 0.0), 1.0)
        funding = item.funding_rate or 0.0
        momentum_score = 0.0
        if funding > 0:
            momentum_score += 0.2
        if item.volume_24h and item.volume_24h > 0:
            momentum_score += 0.2
        return MarketFeatureVectorV11(
            symbol=item.normalized_symbol,
            last_price=last,
            volume_24h=item.volume_24h,
            spread=item.spread,
            funding_rate=item.funding_rate,
            open_interest=item.open_interest,
            volatility_score=volatility_score,
            momentum_score=min(momentum_score, 1.0),
        )
