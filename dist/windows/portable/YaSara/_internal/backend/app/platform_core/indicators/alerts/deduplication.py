class IndicatorAlertDeduplicator:
    def __init__(self):
        self._seen = set()

    def key(self, symbol: str, direction: str, confidence: int):
        bucket = int(confidence / 10) * 10
        return f"{symbol}:{direction}:{bucket}"

    def should_emit(self, symbol: str, direction: str, confidence: int):
        k = self.key(symbol, direction, confidence)
        if k in self._seen:
            return False
        self._seen.add(k)
        return True

indicator_alert_deduplicator = IndicatorAlertDeduplicator()
