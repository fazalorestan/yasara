from app.v11_strategy_runtime.models import StrategyContextV11
from app.v11_ai_market_intelligence.service import AIMarketIntelligenceServiceV11
from app.v11_market_data.service import MarketDataServiceV11


class StrategyContextBuilderV11:
    def demo_context(self, symbol: str = "BTCUSDT") -> StrategyContextV11:
        market = MarketDataServiceV11()
        market.bootstrap_demo()
        item = market.engine.cache.get("binance", symbol)
        price = item.last_price if item and item.last_price else 100.0

        ai_payload = AIMarketIntelligenceServiceV11().dashboard_payload()
        ai_score = 0.0
        for insight in ai_payload.get("items", []):
            signal = insight.get("signal", {})
            if signal.get("symbol") == symbol.upper():
                ai_score = float(signal.get("score", 0.0))
                break

        return StrategyContextV11(
            symbol=symbol.upper(),
            price=price,
            ai_score=ai_score,
            risk_allowed=True,
        )
