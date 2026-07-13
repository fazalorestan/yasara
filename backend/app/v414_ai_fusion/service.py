from app.v40_market_context.service import MarketContextServiceV40
from app.v40_market_context.models import MarketContextRequestV40
from app.v410_market_structure_sprint2.service import MarketStructureSprint2ServiceV410
from app.v412_smart_money_pro_sprint2.service import SmartMoneyProSprint2ServiceV412
from app.v413_ict_engine.service import ICTEngineServiceV413
from app.v41_indicator_engine.service import ModularIndicatorEngineServiceV41
from app.v43_risk_engine.service import AdvancedRiskEngineServiceV43
from app.v414_ai_fusion.fusion import fuse_modules, explain
from app.v414_ai_fusion.models import AIDecisionFusionRequestV414, AIDecisionFusionSummaryV414

class AIDecisionFusionServiceV414:
    def __init__(self):
        self.market_context = MarketContextServiceV40()
        self.structure = MarketStructureSprint2ServiceV410()
        self.smart_money = SmartMoneyProSprint2ServiceV412()
        self.ict = ICTEngineServiceV413()
        self.indicator = ModularIndicatorEngineServiceV41()
        self.risk = AdvancedRiskEngineServiceV43()

    def summary(self):
        return AIDecisionFusionSummaryV414()

    def analyze(self, request: AIDecisionFusionRequestV414):
        modules = []

        if request.feature_flags.get("market_context", True):
            ctx = self.market_context.context(MarketContextRequestV40(symbol=request.symbol, exchange=request.exchange, timeframes=[request.timeframe, "5m", "15m", "1h"]))
            modules.append({
                "module": "market_context",
                "bias": ctx["market_context"]["bias"],
                "confidence": ctx["market_context"]["confidence"],
                "reasons": [ctx["market_context"]["regime"], ctx["market_context"]["momentum"]],
            })

        if request.feature_flags.get("market_structure", True):
            st = self.structure.quick(request.symbol, request.exchange)
            modules.append({
                "module": "market_structure",
                "bias": st["engine_output"]["bias"],
                "confidence": st["engine_output"]["confidence"],
                "reasons": st["engine_output"]["reasons"],
            })

        if request.feature_flags.get("smart_money", True):
            smc = self.smart_money.quick(request.symbol, request.exchange, request.timeframe)
            modules.append({
                "module": "smart_money",
                "bias": smc["engine_output"]["bias"],
                "confidence": smc["engine_output"]["confidence"],
                "reasons": smc["engine_output"]["reasons"],
            })

        if request.feature_flags.get("ict", True):
            ict = self.ict.quick(request.symbol, request.exchange, request.timeframe)
            modules.append({
                "module": "ict",
                "bias": ict["engine_output"]["bias"],
                "confidence": ict["engine_output"]["confidence"],
                "reasons": ict["engine_output"]["reasons"],
            })

        if request.feature_flags.get("indicator", True):
            ind = self.indicator.quick(request.symbol, request.exchange, request.timeframe)
            modules.append({
                "module": "indicator",
                "bias": ind["aggregate"]["bias"],
                "confidence": ind["aggregate"]["confidence"],
                "reasons": [f"bullish={ind['aggregate']['bullish_count']}", f"bearish={ind['aggregate']['bearish_count']}"],
            })

        if request.feature_flags.get("risk", True):
            risk = self.risk.signal_risk(request.symbol, request.exchange, request.timeframe)
            risk_allowed = risk["risk"]["guards"]["allowed"]
            modules.append({
                "module": "risk",
                "bias": "bullish" if risk_allowed else "neutral",
                "confidence": 80 if risk_allowed else 35,
                "reasons": risk["risk"]["guards"]["reasons"],
            })

        fusion = fuse_modules(modules)
        explanation = explain(fusion)

        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "fusion": fusion,
            "decision": {
                "action": fusion["decision"],
                "final_score": fusion["final_score"],
                "confidence": fusion["final_confidence"],
                "confidence_class": fusion["confidence_class"],
                "agreement_percent": fusion["agreement"]["agreement_percent"],
                "has_conflict": fusion["conflict"]["has_conflict"],
            },
            "explanation": explanation,
            "constitution_compliant": True,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }

    def quick(self, symbol="BTCUSDT", exchange="binance", timeframe="1m"):
        return self.analyze(AIDecisionFusionRequestV414(symbol=symbol, exchange=exchange, timeframe=timeframe))
