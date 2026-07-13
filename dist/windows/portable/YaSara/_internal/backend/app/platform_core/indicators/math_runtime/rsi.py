class RSIMath:
    def rsi(self, closes: list[float], length: int = 14):
        if length <= 0 or len(closes) <= length:
            return None
        gains = []
        losses = []
        for i in range(-length, 0):
            delta = closes[i] - closes[i - 1]
            gains.append(max(delta, 0))
            losses.append(abs(min(delta, 0)))
        avg_gain = sum(gains) / length
        avg_loss = sum(losses) / length
        if avg_loss == 0:
            return 100.0
        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))

rsi_math = RSIMath()
