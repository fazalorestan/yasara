from app.v32_advanced_ai_indicators.service import AdvancedAIIndicatorServiceV32
from app.v32_advanced_ai_indicators.models import AdvancedIndicatorRequestV32
from app.v33_strategy_builder.engine import StrategyRuleEngineV33
from app.v33_strategy_builder.models import StrategyBuilderSummaryV33, StrategyContextV33, StrategyDefinitionV33
from app.v33_strategy_builder.store import StrategyStoreV33


class StrategyBuilderServiceV33:
    def __init__(self):
        self.store = StrategyStoreV33()
        self.engine = StrategyRuleEngineV33()
        self.ai = AdvancedAIIndicatorServiceV32()

    def summary(self):
        return StrategyBuilderSummaryV33()

    def list_strategies(self):
        return {"ready": True, "items": [item.model_dump() for item in self.store.list()], "live_trading_enabled": False}

    def save_strategy(self, strategy: StrategyDefinitionV33):
        return self.store.save(strategy)

    def get_strategy(self, strategy_id: str):
        strategy = self.store.get(strategy_id)
        return {"ready": strategy is not None, "strategy": strategy.model_dump() if strategy else None}

    def archive_strategy(self, strategy_id: str):
        strategy = self.store.archive(strategy_id)
        return {"ready": strategy is not None, "strategy": strategy.model_dump() if strategy else None}

    def build_context_from_ai(self, symbol: str, exchange: str, timeframe: str):
        analysis = self.ai.analyze(AdvancedIndicatorRequestV32(symbol=symbol, exchange=exchange, timeframe=timeframe, limit=120))
        indicators = analysis["indicators"]
        return {
            "symbol": symbol.upper(),
            "exchange": exchange,
            "timeframe": timeframe,
            "fields": {
                "last_close": analysis["last_close"],
                "ema20": indicators["ema20"],
                "ema50": indicators["ema50"],
                "rsi14": indicators["rsi14"],
                "macd_histogram": indicators["macd"]["histogram"],
                "atr14": indicators["atr14"],
                "ai_score": analysis["ai_signal"]["score"],
                "ai_confidence": analysis["ai_signal"]["confidence"],
            },
            "source": "v33_strategy_context_from_v32_ai",
            "live_trading_enabled": False,
        }

    def evaluate(self, strategy_id: str, context: StrategyContextV33 | None = None):
        strategy = self.store.get(strategy_id)
        if not strategy:
            return {"ready": False, "error": "strategy_not_found", "live_trading_enabled": False}

        if context is None:
            data = self.build_context_from_ai(strategy.symbol, strategy.exchange, strategy.timeframe)
            fields = data["fields"]
        else:
            fields = context.fields

        return self.engine.evaluate_strategy(strategy, fields)

    def demo_strategy(self):
        strategy = StrategyDefinitionV33(
            strategy_id="demo-ema-rsi",
            name="Demo EMA RSI Strategy",
            symbol="BTCUSDT",
            exchange="binance",
            timeframe="1m",
            status="active",
            rules=[
                {
                    "rule_id": "rule-long-1",
                    "name": "EMA bullish and RSI healthy",
                    "conditions": [
                        {"left": "ema20", "operator": "gt", "right": "ema50"},
                        {"left": "rsi14", "operator": "lt", "right": 70},
                        {"left": "ai_score", "operator": "gte", "right": 55}
                    ],
                    "action": "buy",
                    "enabled": True
                },
                {
                    "rule_id": "rule-short-1",
                    "name": "EMA bearish and weak AI score",
                    "conditions": [
                        {"left": "ema20", "operator": "lt", "right": "ema50"},
                        {"left": "ai_score", "operator": "lte", "right": 45}
                    ],
                    "action": "sell",
                    "enabled": True
                }
            ]
        )
        return self.save_strategy(strategy)
