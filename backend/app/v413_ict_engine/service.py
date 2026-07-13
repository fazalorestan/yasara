from app.v31_live_exchange.service import LiveExchangeServiceV31
from app.v410_market_structure_sprint2.service import MarketStructureSprint2ServiceV410
from app.v412_smart_money_pro_sprint2.service import SmartMoneyProSprint2ServiceV412
from app.v413_ict_engine.detectors import ict_context_score, ict_liquidity_model, judas_swing, kill_zone, ote_zone, power_of_three
from app.v413_ict_engine.models import ICTEngineRequestV413, ICTEngineSummaryV413

class ICTEngineServiceV413:
    def __init__(self):
        self.live = LiveExchangeServiceV31()
        self.structure = MarketStructureSprint2ServiceV410()
        self.smc = SmartMoneyProSprint2ServiceV412()

    def summary(self):
        return ICTEngineSummaryV413()

    def analyze(self, request: ICTEngineRequestV413):
        candles = self.live.live_candles(request.symbol, request.exchange, request.timeframe, request.limit)["candles"]
        structure = self.structure.quick(request.symbol, request.exchange)
        smc = self.smc.quick(request.symbol, request.exchange, request.timeframe)
        last_ts = candles[-1]["time"] if candles else 0

        kz = kill_zone(last_ts)
        judas = judas_swing(candles, structure["multi_timeframe_structure"]["bias"])
        po3 = power_of_three(candles)
        ote = ote_zone(candles)
        liquidity = ict_liquidity_model(structure, smc)
        score = ict_context_score(kz, judas, po3, ote, liquidity)

        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "ict": {
                "kill_zone": kz,
                "judas_swing": judas,
                "power_of_three": po3,
                "ote": ote,
                "liquidity_model": liquidity,
                "context_score": score,
            },
            "engine_output": {
                "engine": "ict_engine_v4_13",
                "bias": score["bias"],
                "confidence": score["score"],
                "reasons": score["reasons"],
            },
            "constitution_compliant": True,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }

    def quick(self, symbol="BTCUSDT", exchange="binance", timeframe="1m"):
        return self.analyze(ICTEngineRequestV413(symbol=symbol, exchange=exchange, timeframe=timeframe))
