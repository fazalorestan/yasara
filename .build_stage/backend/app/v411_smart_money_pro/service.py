from app.v31_live_exchange.service import LiveExchangeServiceV31
from app.v410_market_structure_sprint2.service import MarketStructureSprint2ServiceV410
from app.v411_smart_money_pro.detectors import breaker_candidates, fair_value_gaps, imbalance_zones, mitigation_status, order_blocks, smart_money_score
from app.v411_smart_money_pro.models import SmartMoneyProRequestV411, SmartMoneyProSummaryV411

class SmartMoneyProServiceV411:
    def __init__(self):
        self.live = LiveExchangeServiceV31()
        self.structure = MarketStructureSprint2ServiceV410()

    def summary(self):
        return SmartMoneyProSummaryV411()

    def analyze(self, request: SmartMoneyProRequestV411):
        candles = self.live.live_candles(request.symbol, request.exchange, request.timeframe, request.limit)["candles"]
        structure = self.structure.quick(request.symbol, request.exchange)
        structure_bias = structure["multi_timeframe_structure"]["bias"]

        obs = order_blocks(candles, structure_bias)
        fvgs = fair_value_gaps(candles)
        imbs = imbalance_zones(candles)
        obs_m = mitigation_status(candles, obs)
        fvgs_m = mitigation_status(candles, fvgs)
        breakers = breaker_candidates(obs_m)
        score = smart_money_score(obs_m, fvgs_m, imbs, breakers, structure_bias)

        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "smart_money_pro": {
                "order_blocks": obs_m,
                "fair_value_gaps": fvgs_m,
                "imbalances": imbs,
                "breaker_candidates": breakers,
                "structure_bias": structure_bias,
                "context_score": score,
            },
            "engine_output": {
                "engine": "smart_money_pro_v4_11",
                "bias": score["bias"],
                "confidence": score["score"],
                "reasons": score["reasons"],
            },
            "constitution_compliant": True,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }

    def quick(self, symbol="BTCUSDT", exchange="binance", timeframe="1m"):
        return self.analyze(SmartMoneyProRequestV411(symbol=symbol, exchange=exchange, timeframe=timeframe))
