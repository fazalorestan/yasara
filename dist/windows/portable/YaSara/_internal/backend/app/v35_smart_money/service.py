from app.v31_live_exchange.service import LiveExchangeServiceV31
from app.v35_smart_money.detectors import (
    detect_bos,
    detect_choch,
    detect_equal_high_low,
    detect_fvg,
    detect_imbalance,
    detect_liquidity_sweep,
    detect_order_block,
    premium_discount,
    score_smart_money,
)
from app.v35_smart_money.models import SmartMoneyRequestV35, SmartMoneySummaryV35


class SmartMoneyEngineServiceV35:
    def __init__(self):
        self.live = LiveExchangeServiceV31()

    def summary(self):
        return SmartMoneySummaryV35()

    def analyze(self, request: SmartMoneyRequestV35):
        candles_payload = self.live.live_candles(
            symbol=request.symbol,
            exchange=request.exchange,
            timeframe=request.timeframe,
            limit=request.limit,
        )
        candles = candles_payload["candles"]

        bos = detect_bos(candles)
        choch = detect_choch(candles)
        sweep = detect_liquidity_sweep(candles)
        order_block = detect_order_block(candles)
        fvg = detect_fvg(candles)
        imbalance = detect_imbalance(candles)
        equal_levels = detect_equal_high_low(candles)
        pd = premium_discount(candles)
        score = score_smart_money(bos, choch, sweep, order_block, fvg, pd)

        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "feature_flags": request.feature_flags,
            "smart_money": {
                "break_of_structure": bos,
                "change_of_character": choch,
                "liquidity_sweep": sweep,
                "liquidity_grab": sweep,
                "order_block": order_block,
                "fair_value_gap": fvg,
                "imbalance": imbalance,
                "premium_discount": pd,
                "equal_high_low": equal_levels,
            },
            "score": score,
            "constitution_compliant": True,
            "live_trading_enabled": False,
        }

    def quick(self, symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m"):
        return self.analyze(SmartMoneyRequestV35(symbol=symbol, exchange=exchange, timeframe=timeframe))
