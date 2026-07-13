from app.v32_advanced_ai_indicators.models import AdvancedIndicatorRequestV32
from app.v32_advanced_ai_indicators.service import AdvancedAIIndicatorServiceV32
from app.v35_smart_money.service import SmartMoneyEngineServiceV35
from app.v40_market_context.models import AutoTradeGateRequestV40, MarketContextRequestV40
from app.v40_market_context.service import MarketContextServiceV40
from app.v41_indicator_engine.service import ModularIndicatorEngineServiceV41
from app.v42_signal_engine.models import SignalEngineSummaryV42, SignalRequestV42
from app.v42_signal_engine.scoring import SignalScoringEngineV42


class MultiLayerSignalEngineServiceV42:
    def __init__(self):
        self.market_context = MarketContextServiceV40()
        self.indicators = ModularIndicatorEngineServiceV41()
        self.smart_money = SmartMoneyEngineServiceV35()
        self.ai = AdvancedAIIndicatorServiceV32()
        self.scoring = SignalScoringEngineV42()

    def summary(self):
        return SignalEngineSummaryV42()

    def _risk_gate(self, merged, request):
        allowed = request.risk_guard_enabled and not request.kill_switch_active and merged["risk"] != "high"
        return {
            "enabled": True,
            "allowed": allowed,
            "risk_label": merged["risk"],
            "kill_switch_active": request.kill_switch_active,
            "risk_guard_enabled": request.risk_guard_enabled,
            "reason": "risk_gate_passed" if allowed else "risk_gate_blocked",
        }

    def generate(self, request: SignalRequestV42):
        layers = []

        if request.feature_flags.get("market_context", True):
            ctx = self.market_context.context(MarketContextRequestV40(
                symbol=request.symbol,
                exchange=request.exchange,
                timeframes=[request.timeframe, "5m", "15m", "1h", "4h"],
            ))
            layers.append({
                "engine": "market_context",
                "enabled": True,
                "bias": ctx["market_context"]["bias"],
                "confidence": ctx["market_context"]["confidence"],
                "weight": 1.25,
                "reasons": [
                    f"regime={ctx['market_context']['regime']}",
                    f"volatility={ctx['market_context']['volatility']}",
                    f"momentum={ctx['market_context']['momentum']}",
                ],
            })
        else:
            ctx = None

        if request.feature_flags.get("indicator_engine", True):
            ind = self.indicators.quick(request.symbol, request.exchange, request.timeframe)
            layers.append({
                "engine": "indicator_engine",
                "enabled": True,
                "bias": ind["aggregate"]["bias"],
                "confidence": ind["aggregate"]["confidence"],
                "weight": 1.15,
                "reasons": [
                    f"indicator_bullish={ind['aggregate']['bullish_count']}",
                    f"indicator_bearish={ind['aggregate']['bearish_count']}",
                ],
            })
        else:
            ind = None

        if request.feature_flags.get("smart_money", True):
            sm = self.smart_money.quick(request.symbol, request.exchange, request.timeframe)
            layers.append({
                "engine": "smart_money",
                "enabled": True,
                "bias": sm["score"]["bias"],
                "confidence": sm["score"]["score"],
                "weight": 1.2,
                "reasons": sm["score"]["reasons"],
            })
        else:
            sm = None

        if request.feature_flags.get("ai_indicators", True):
            ai = self.ai.analyze(AdvancedIndicatorRequestV32(
                symbol=request.symbol,
                exchange=request.exchange,
                timeframe=request.timeframe,
                limit=120,
            ))
            ai_bias = "bullish" if ai["ai_signal"]["direction"] == "long" else "bearish" if ai["ai_signal"]["direction"] == "short" else "neutral"
            layers.append({
                "engine": "advanced_ai_indicators",
                "enabled": True,
                "bias": ai_bias,
                "confidence": ai["ai_signal"]["confidence"],
                "weight": 1.0,
                "reasons": ai["ai_signal"]["reasons"],
            })
        else:
            ai = None

        merged = self.scoring.merge(layers)
        risk_gate = self._risk_gate(merged, request)

        auto_gate = self.market_context.autotrade_gate(AutoTradeGateRequestV40(
            build_type=request.build_type,
            license_key=request.license_key,
            exchange=request.exchange,
            has_exchange_api_key=request.has_exchange_api_key,
            risk_guard_enabled=risk_gate["allowed"],
            kill_switch_active=request.kill_switch_active,
            checkbox_enabled=request.autotrade_checkbox_enabled,
        ))

        execution_allowed = risk_gate["allowed"] and auto_gate["allowed"] and request.build_type == "personal"

        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "signal": {
                "action": merged["action"],
                "direction": merged["direction"],
                "score": merged["score"],
                "confidence": merged["confidence"],
                "risk": merged["risk"],
                "execution_allowed": execution_allowed,
                "real_order_execution_enabled": False,
            },
            "layers": layers,
            "votes": merged["votes"],
            "reasons": merged["reasons"],
            "risk_gate": risk_gate,
            "autotrade_gate": auto_gate,
            "commercial_execution_included": False,
            "constitution_compliant": True,
            "live_trading_enabled": False,
        }

    def quick(self, symbol="BTCUSDT", exchange="binance", timeframe="1m"):
        return self.generate(SignalRequestV42(symbol=symbol, exchange=exchange, timeframe=timeframe))
