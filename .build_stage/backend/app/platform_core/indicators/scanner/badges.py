class IndicatorSignalBadgeAdapter:
    def badge(self, direction: str, score: int):
        direction = direction.upper()
        if direction == "LONG" and score >= 65:
            return "▲ LONG"
        if direction == "SHORT" and score >= 65:
            return "▼ SHORT"
        if score >= 50:
            return "WATCH"
        return "WAIT"

indicator_signal_badge_adapter = IndicatorSignalBadgeAdapter()
