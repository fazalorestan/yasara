from app.v34_market_analysis.service import MarketAnalysisEngineServiceV34
from app.v35_smart_money.service import SmartMoneyEngineServiceV35
from app.v32_advanced_ai_indicators.service import AdvancedAIIndicatorServiceV32
from app.v40_market_context.autotrade_gate import AutoTradeGateV40
from app.v40_market_context.models import AutoTradeGateRequestV40, EngineResultV40, MarketContextRequestV40, MarketContextSummaryV40
from app.v40_market_context.normalizer import ConfidenceNormalizerV40
from app.v40_market_context.registry import EngineRegistryV40


class MarketContextServiceV40:
    def __init__(self):
        self.market = MarketAnalysisEngineServiceV34()
        self.smart = SmartMoneyEngineServiceV35()
        self.ai = AdvancedAIIndicatorServiceV32()
        self.normalizer = ConfidenceNormalizerV40()
        self.registry = EngineRegistryV40()
        self.autotrade = AutoTradeGateV40()

    def summary(self):
        return MarketContextSummaryV40()

    def engines(self):
        return self.registry.list()

    def context(self, request: MarketContextRequestV40):
        market = self.market.analyze_timeframe(request.symbol, request.exchange, request.timeframes[-1], 120)
        smart = self.smart.quick(request.symbol, request.exchange, request.timeframes[0])
        ai = self.ai.analyze(__import__("app.v32_advanced_ai_indicators.models", fromlist=["AdvancedIndicatorRequestV32"]).AdvancedIndicatorRequestV32(
            symbol=request.symbol,
            exchange=request.exchange,
            timeframe=request.timeframes[0],
            limit=120,
        ))

        results = [
            EngineResultV40(
                engine="market_analysis",
                confidence=market["trend"]["strength"],
                bias=market["trend"]["trend"] if market["trend"]["trend"] in ["bullish", "bearish"] else "neutral",
                weight=1.2,
                reasons=[f"regime={market['regime']}", f"momentum={market['momentum']['momentum']}"],
            ),
            EngineResultV40(
                engine="smart_money",
                confidence=smart["score"]["score"],
                bias=smart["score"]["bias"],
                weight=1.1,
                reasons=smart["score"]["reasons"],
            ),
            EngineResultV40(
                engine="advanced_ai_indicators",
                confidence=ai["ai_signal"]["confidence"],
                bias="bullish" if ai["ai_signal"]["direction"] == "long" else "bearish" if ai["ai_signal"]["direction"] == "short" else "neutral",
                weight=1.0,
                reasons=ai["ai_signal"]["reasons"],
            ),
        ]

        merged = self.normalizer.weighted_score(results)
        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframes": request.timeframes,
            "market_context": {
                "bias": merged["bias"],
                "confidence": merged["score"],
                "regime": market["regime"],
                "volatility": market["volatility"]["volatility"],
                "momentum": market["momentum"]["momentum"],
                "volume": market["volume"]["volume_state"],
                "session": market["session"]["session"],
            },
            "engine_results": [r.model_dump() for r in results],
            "engine_registry": self.registry.enabled_engines(),
            "constitution_compliant": True,
            "live_trading_enabled": False,
        }

    def autotrade_gate(self, request: AutoTradeGateRequestV40):
        return self.autotrade.validate(request)
