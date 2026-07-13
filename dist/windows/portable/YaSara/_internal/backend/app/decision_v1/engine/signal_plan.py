from app.decision_v1.domain.models import DecisionDirection, SignalPlan
from app.intelligence_v1.domain.models import MarketIntelligenceReport

class SignalPlanBuilderV1:
    def build(self, report: MarketIntelligenceReport, direction: DecisionDirection) -> SignalPlan:
        if direction not in {DecisionDirection.LONG, DecisionDirection.SHORT} or not report.timeframes:
            return SignalPlan(invalidation="No directional signal plan because decision is WAIT/NO_TRADE.")

        latest = list(report.timeframes.values())[-1]
        indicators = latest.indicators
        atr = indicators.atr_14 or 0
        last_price = self._last_proxy_price(latest)
        if not last_price:
            return SignalPlan(invalidation="Price proxy unavailable.")

        entry_low = last_price - atr * 0.25 if atr else last_price * 0.998
        entry_high = last_price + atr * 0.25 if atr else last_price * 1.002

        if direction == DecisionDirection.LONG:
            sl = last_price - (atr * 1.5 if atr else last_price * 0.01)
            tp1 = last_price + (atr * 1.5 if atr else last_price * 0.015)
            tp2 = last_price + (atr * 2.5 if atr else last_price * 0.025)
            tp3 = last_price + (atr * 4.0 if atr else last_price * 0.04)
            invalidation = "Invalid if price closes below stop loss or market structure turns bearish."
        else:
            sl = last_price + (atr * 1.5 if atr else last_price * 0.01)
            tp1 = last_price - (atr * 1.5 if atr else last_price * 0.015)
            tp2 = last_price - (atr * 2.5 if atr else last_price * 0.025)
            tp3 = last_price - (atr * 4.0 if atr else last_price * 0.04)
            invalidation = "Invalid if price closes above stop loss or market structure turns bullish."

        return SignalPlan(
            entry_zone_low=min(entry_low, entry_high),
            entry_zone_high=max(entry_low, entry_high),
            stop_loss=sl,
            tp1=tp1,
            tp2=tp2,
            tp3=tp3,
            invalidation=invalidation,
            lifetime_minutes=60,
        )

    def _last_proxy_price(self, latest) -> float | None:
        sma = latest.indicators.sma_20
        ema = latest.indicators.ema_20
        if sma and ema:
            return (sma + ema) / 2
        return sma or ema
