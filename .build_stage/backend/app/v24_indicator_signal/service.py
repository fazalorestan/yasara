from app.v23_exchange_connector.service import ExchangeConnectorServiceV23
from app.v24_indicator_signal.math import ema, macd, rsi
from app.v24_indicator_signal.models import IndicatorSummaryV24, IndicatorSnapshotV24


class IndicatorSignalServiceV24:
    def __init__(self):
        self.exchange = ExchangeConnectorServiceV23()

    def summary(self):
        return IndicatorSummaryV24()

    def snapshot(self, symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "4H"):
        ohlc = self.exchange.ohlc_live_ready(symbol=symbol, exchange=exchange, timeframe=timeframe, limit=120)
        closes = [c["close"] for c in ohlc["candles"]]
        ema_fast = ema(closes, 12)
        ema_slow = ema(closes, 26)
        rsi_value = rsi(closes, 14)
        macd_value, macd_signal = macd(closes)

        trend = "bullish" if ema_fast > ema_slow else "bearish" if ema_fast < ema_slow else "neutral"
        signal = "neutral"
        confidence = 55

        if trend == "bullish" and rsi_value < 70 and macd_value >= macd_signal:
            signal = "bullish"
            confidence = 78
        elif trend == "bearish" and rsi_value > 30 and macd_value <= macd_signal:
            signal = "bearish"
            confidence = 74
        elif rsi_value >= 70 or rsi_value <= 30:
            signal = "volatile"
            confidence = 68

        return IndicatorSnapshotV24(
            symbol=symbol.upper(),
            exchange=exchange,
            timeframe=timeframe,
            ema_fast=ema_fast,
            ema_slow=ema_slow,
            rsi=rsi_value,
            macd=macd_value,
            macd_signal=macd_signal,
            trend=trend,
            signal=signal,
            confidence=confidence,
        )

    def batch(self, exchange: str = "all"):
        symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT"]
        return {
            "ready": True,
            "items": [self.snapshot(symbol=s, exchange="binance" if s != "SOLUSDT" else "toobit").model_dump() for s in symbols],
            "live_trading_enabled": False,
        }
