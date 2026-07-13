from app.v41_indicator_engine import calculations as calc

class ModularIndicatorRegistryV41:
    def __init__(self):
        self.registry = {
            "ema": self._ema,
            "sma": self._sma,
            "rsi": self._rsi,
            "macd": self._macd,
            "atr": self._atr,
            "adx": self._adx,
            "supertrend": self._supertrend,
            "vwap": self._vwap,
            "bollinger": self._bollinger,
            "obv": self._obv,
            "mfi": self._mfi,
            "cci": self._cci,
            "stochastic": self._stochastic,
            "donchian": self._donchian,
            "keltner": self._keltner,
            "parabolic_sar": self._parabolic_sar,
        }

    def names(self):
        return list(self.registry.keys())

    def compute(self, name, candles):
        return self.registry[name](candles)

    def _bias_from_pair(self, fast, slow):
        return "bullish" if fast > slow else "bearish" if fast < slow else "neutral"

    def _ema(self, candles):
        c = calc.closes(candles); e20, e50 = calc.ema(c,20), calc.ema(c,50)
        return {"ema20": e20, "ema50": e50}, self._bias_from_pair(e20,e50), 70

    def _sma(self, candles):
        c = calc.closes(candles); s20, s50 = calc.sma(c,20), calc.sma(c,50)
        return {"sma20": s20, "sma50": s50}, self._bias_from_pair(s20,s50), 65

    def _rsi(self, candles):
        value = calc.rsi(calc.closes(candles))
        bias = "bullish" if value < 35 else "bearish" if value > 70 else "neutral"
        return {"rsi14": value}, bias, 60

    def _macd(self, candles):
        value = calc.macd(calc.closes(candles))
        return value, "bullish" if value["histogram"] > 0 else "bearish" if value["histogram"] < 0 else "neutral", 65

    def _atr(self, candles):
        return {"atr14": calc.atr(candles)}, "neutral", 50

    def _adx(self, candles):
        value = calc.adx(candles)
        return {"adx14": value}, "neutral", min(100, value)

    def _supertrend(self, candles):
        value = calc.supertrend(candles)
        return value, value["trend"], 70

    def _vwap(self, candles):
        value = calc.vwap(candles); close = candles[-1]["close"] if candles else 0
        return {"vwap": value}, "bullish" if close > value else "bearish" if close < value else "neutral", 60

    def _bollinger(self, candles):
        value = calc.bollinger(calc.closes(candles)); close = candles[-1]["close"] if candles else 0
        bias = "bullish" if close <= value["lower"] else "bearish" if close >= value["upper"] else "neutral"
        return value, bias, 55

    def _obv(self, candles):
        return {"obv": calc.obv(candles)}, "neutral", 50

    def _mfi(self, candles):
        value = calc.mfi(candles)
        return {"mfi": value}, "bullish" if value < 25 else "bearish" if value > 80 else "neutral", 55

    def _cci(self, candles):
        value = calc.cci(candles)
        return {"cci": value}, "bullish" if value < -100 else "bearish" if value > 100 else "neutral", 55

    def _stochastic(self, candles):
        value = calc.stochastic(candles)
        return value, "bullish" if value["k"] < 20 else "bearish" if value["k"] > 80 else "neutral", 55

    def _donchian(self, candles):
        value = calc.donchian(candles)
        close = candles[-1]["close"] if candles else 0
        return value, "bullish" if close > value["middle"] else "bearish" if close < value["middle"] else "neutral", 55

    def _keltner(self, candles):
        value = calc.keltner(candles)
        close = candles[-1]["close"] if candles else 0
        return value, "bullish" if close > value["middle"] else "bearish" if close < value["middle"] else "neutral", 55

    def _parabolic_sar(self, candles):
        value = calc.parabolic_sar(candles)
        return value, value["trend"], 55
