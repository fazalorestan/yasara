from app.platform_core.indicators.scanner.badges import indicator_signal_badge_adapter
from app.platform_core.indicators.scanner.ranking import indicator_ranking_service

class IndicatorWatchlistAdapter:
    def from_bridge_output(self, bridge_output: dict):
        scanner = bridge_output.get("scanner", {})
        score = int(scanner.get("score", 0))
        direction = scanner.get("direction", "WAIT")
        return {
            "symbol": scanner.get("symbol", "UNKNOWN"),
            "indicator": "yasara",
            "direction": direction,
            "score": score,
            "grade": indicator_ranking_service.grade(score),
            "badge": indicator_signal_badge_adapter.badge(direction, score),
            "execution_allowed": False,
            "mode": "analysis_only",
        }

indicator_watchlist_adapter = IndicatorWatchlistAdapter()
