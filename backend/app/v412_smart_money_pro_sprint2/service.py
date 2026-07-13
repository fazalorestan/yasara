from app.v31_live_exchange.service import LiveExchangeServiceV31
from app.v410_market_structure_sprint2.service import MarketStructureSprint2ServiceV410
from app.v411_smart_money_pro.service import SmartMoneyProServiceV411
from app.v412_smart_money_pro_sprint2.detectors import (
    entry_quality_score,
    liquidity_grab,
    ob_fvg_confluence,
    premium_discount_entry,
    sweep_pro,
)
from app.v412_smart_money_pro_sprint2.models import SmartMoneyProSprint2RequestV412, SmartMoneyProSprint2SummaryV412

class SmartMoneyProSprint2ServiceV412:
    def __init__(self):
        self.live = LiveExchangeServiceV31()
        self.structure = MarketStructureSprint2ServiceV410()
        self.smc = SmartMoneyProServiceV411()

    def summary(self):
        return SmartMoneyProSprint2SummaryV412()

    def analyze(self, request: SmartMoneyProSprint2RequestV412):
        candles = self.live.live_candles(request.symbol, request.exchange, request.timeframe, request.limit)["candles"]
        structure = self.structure.quick(request.symbol, request.exchange)
        smc = self.smc.quick(request.symbol, request.exchange, request.timeframe)

        first_tf = structure["items"][0]
        liquidity_zones = first_tf["liquidity_zones"]
        basic_sweep = first_tf["liquidity_sweep"]
        pd_context = first_tf["base_structure"]["premium_discount"]
        structure_bias = structure["multi_timeframe_structure"]["bias"]
        smc_bias = smc["engine_output"]["bias"]

        grab = liquidity_grab(candles, liquidity_zones)
        sweep = sweep_pro(candles, basic_sweep, grab)
        direction = sweep.get("direction") if sweep.get("detected") else smc_bias
        pd_entry = premium_discount_entry(pd_context, direction)
        confluence = ob_fvg_confluence(
            smc["smart_money_pro"]["order_blocks"],
            smc["smart_money_pro"]["fair_value_gaps"],
        )
        quality = entry_quality_score(sweep, pd_entry, confluence, structure_bias, smc_bias)

        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "smart_money_pro_sprint2": {
                "liquidity_grab": grab,
                "sweep_pro": sweep,
                "premium_discount_entry": pd_entry,
                "ob_fvg_confluence": confluence,
                "structure_bias": structure_bias,
                "smc_bias": smc_bias,
                "entry_quality": quality,
            },
            "engine_output": {
                "engine": "smart_money_pro_v4_12",
                "bias": quality["bias"],
                "confidence": quality["score"],
                "risk": quality["risk"],
                "reasons": quality["reasons"],
            },
            "constitution_compliant": True,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }

    def quick(self, symbol="BTCUSDT", exchange="binance", timeframe="1m"):
        return self.analyze(SmartMoneyProSprint2RequestV412(symbol=symbol, exchange=exchange, timeframe=timeframe))
