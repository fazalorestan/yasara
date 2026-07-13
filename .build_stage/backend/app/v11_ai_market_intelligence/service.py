from app.v11_ai_market_intelligence.insight_engine import AIMarketInsightEngineV11
from app.v11_market_data.service import MarketDataServiceV11


class AIMarketIntelligenceServiceV11:
    def __init__(self):
        self.market_data = MarketDataServiceV11()
        self.engine = AIMarketInsightEngineV11()

    def demo_insights(self):
        self.market_data.bootstrap_demo()
        snapshot = self.market_data.engine.snapshot()
        return [self.engine.analyze_item(item) for item in snapshot.items]

    def dashboard_payload(self) -> dict:
        insights = self.demo_insights()
        return {
            "ready": bool(insights),
            "count": len(insights),
            "items": [insight.model_dump() for insight in insights],
            "safety": "analysis_only_no_trade_execution",
        }
