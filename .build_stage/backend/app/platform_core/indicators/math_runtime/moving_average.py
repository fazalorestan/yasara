class MovingAverageMath:
    def sma(self, values: list[float], length: int):
        if length <= 0 or len(values) < length:
            return None
        return sum(values[-length:]) / length

    def ema_series(self, values: list[float], length: int):
        if length <= 0 or not values:
            return []
        k = 2 / (length + 1)
        out = [values[0]]
        for value in values[1:]:
            out.append(value * k + out[-1] * (1 - k))
        return out

    def ema(self, values: list[float], length: int):
        series = self.ema_series(values, length)
        return series[-1] if series else None

moving_average_math = MovingAverageMath()
