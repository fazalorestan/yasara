from app.v31_live_exchange.service import LiveExchangeServiceV31
from app.v49_market_structure.models import MarketStructureRequestV49
from app.v49_market_structure.service import ProfessionalMarketStructureServiceV49
from app.v410_market_structure_sprint2.detectors import classify_internal_external, liquidity_sweep, liquidity_zones, mtf_context, structure_strength
from app.v410_market_structure_sprint2.models import MarketStructureSprint2RequestV410, MarketStructureSprint2SummaryV410

class MarketStructureSprint2ServiceV410:
    def __init__(self):
        self.live = LiveExchangeServiceV31()
        self.v49 = ProfessionalMarketStructureServiceV49()

    def summary(self):
        return MarketStructureSprint2SummaryV410()

    def analyze_timeframe(self, symbol, exchange, timeframe, limit, tolerance):
        base = self.v49.analyze(MarketStructureRequestV49(symbol=symbol, exchange=exchange, timeframe=timeframe, limit=limit))
        candles = self.live.live_candles(symbol=symbol, exchange=exchange, timeframe=timeframe, limit=limit)["candles"]
        swings = {"highs": base["structure"]["swings"]["highs"], "lows": base["structure"]["swings"]["lows"]}
        scope = classify_internal_external(swings)
        zones = liquidity_zones(swings, tolerance)
        sweep = liquidity_sweep(candles, zones)
        strength = structure_strength(base, zones, sweep)
        return {"timeframe": timeframe, "base_structure": base["structure"], "structure_scope": scope, "liquidity_zones": zones, "liquidity_sweep": sweep, "strength": strength}

    def analyze(self, request: MarketStructureSprint2RequestV410):
        items = [self.analyze_timeframe(request.symbol, request.exchange, tf, request.limit, request.equal_tolerance_percent) for tf in request.timeframes]
        mtf = mtf_context(items)
        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframes": request.timeframes,
            "items": items,
            "multi_timeframe_structure": mtf,
            "engine_output": {"engine": "market_structure_v4_10", "bias": mtf["bias"], "confidence": mtf["alignment_percent"], "reasons": ["internal_external_structure", "liquidity_mapping", "mtf_structure_context"]},
            "constitution_compliant": True,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }

    def quick(self, symbol="BTCUSDT", exchange="binance"):
        return self.analyze(MarketStructureSprint2RequestV410(symbol=symbol, exchange=exchange))
