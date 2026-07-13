from app.v31_live_exchange.service import LiveExchangeServiceV31
from app.v32_advanced_ai_indicators.math import atr, bollinger, ema, ichimoku, macd, rsi, supertrend
from app.v32_advanced_ai_indicators.models import AdvancedAIIndicatorSummaryV32, AdvancedIndicatorRequestV32


class AdvancedAIIndicatorServiceV32:
    def __init__(self):
        self.live = LiveExchangeServiceV31()

    def summary(self):
        return AdvancedAIIndicatorSummaryV32()

    def analyze(self, request: AdvancedIndicatorRequestV32):
        candles_payload = self.live.live_candles(
            symbol=request.symbol,
            exchange=request.exchange,
            timeframe=request.timeframe,
            limit=request.limit,
        )
        candles = candles_payload["candles"]
        closes = [c["close"] for c in candles]
        last_close = closes[-1] if closes else 0

        ema20 = ema(closes, 20)
        ema50 = ema(closes, 50)
        rsi14 = rsi(closes, 14)
        macd_line, macd_signal, macd_hist = macd(closes)
        atr14 = atr(candles, 14)
        bb = bollinger(closes)
        st = supertrend(candles)
        ichi = ichimoku(candles)

        score = 50
        reasons = []
        if ema20 > ema50:
            score += 10
            reasons.append("EMA20 above EMA50")
        else:
            score -= 10
            reasons.append("EMA20 below EMA50")
        if rsi14 < 30:
            score += 8
            reasons.append("RSI oversold")
        elif rsi14 > 70:
            score -= 8
            reasons.append("RSI overbought")
        if macd_hist > 0:
            score += 8
            reasons.append("MACD histogram positive")
        else:
            score -= 8
            reasons.append("MACD histogram negative")
        if st["trend"] == "bullish":
            score += 7
            reasons.append("SuperTrend bullish")
        else:
            score -= 7
            reasons.append("SuperTrend bearish")
        if ichi["cloud"] == "bullish":
            score += 7
            reasons.append("Price above Ichimoku cloud")
        elif ichi["cloud"] == "bearish":
            score -= 7
            reasons.append("Price below Ichimoku cloud")

        score = max(0, min(100, score))
        direction = "long" if score >= 62 else "short" if score <= 38 else "wait"
        confidence = abs(score - 50) + 50 if direction != "wait" else 55
        confidence = min(95, int(confidence))

        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "last_close": last_close,
            "indicators": {
                "ema20": ema20,
                "ema50": ema50,
                "rsi14": rsi14,
                "macd": {"line": macd_line, "signal": macd_signal, "histogram": macd_hist},
                "atr14": atr14,
                "bollinger": bb,
                "supertrend": st,
                "ichimoku": ichi,
            },
            "ai_signal": {
                "direction": direction,
                "score": score,
                "confidence": confidence,
                "reasons": reasons,
            },
            "explanation": f"YaSara AI score is {score}; direction is {direction}; confidence is {confidence}%.",
            "live_trading_enabled": False,
        }

    def batch(self):
        symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT"]
        return {
            "ready": True,
            "items": [self.analyze(AdvancedIndicatorRequestV32(symbol=s, exchange='binance' if s != 'SOLUSDT' else 'toobit')) for s in symbols],
            "live_trading_enabled": False,
        }
