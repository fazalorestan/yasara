class SignalReasonCodeMapper:
    mapping = {
        "ema21_above_ema55": "TREND_BULLISH",
        "ema21_below_ema55": "TREND_BEARISH",
        "rsi_bullish": "MOMENTUM_RSI_BULLISH",
        "rsi_bearish": "MOMENTUM_RSI_BEARISH",
        "macd_hist_positive": "MOMENTUM_MACD_POSITIVE",
        "macd_hist_negative": "MOMENTUM_MACD_NEGATIVE",
        "atr_available": "VOLATILITY_ACTIVE",
    }

    def map(self, reasons: list[str]):
        output = []
        for reason in reasons:
            for part in str(reason).split(","):
                if part:
                    output.append(self.mapping.get(part, "UNKNOWN_REASON"))
        return output or ["NO_CLEAR_REASON"]

signal_reason_code_mapper = SignalReasonCodeMapper()
