class ATRMath:
    def atr(self, highs: list[float], lows: list[float], closes: list[float], length: int = 14):
        if length <= 0 or len(highs) <= length or len(lows) <= length or len(closes) <= length:
            return None
        trs = []
        for i in range(1, len(closes)):
            trs.append(max(
                highs[i] - lows[i],
                abs(highs[i] - closes[i - 1]),
                abs(lows[i] - closes[i - 1]),
            ))
        if len(trs) < length:
            return None
        return sum(trs[-length:]) / length

atr_math = ATRMath()
