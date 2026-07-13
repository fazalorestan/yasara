from app.production_ai_v1.domain.models import JournalAnalytics, TradingJournalEntry

class JournalAnalyticsEngineV1:
    def analyze(self, entries: list[TradingJournalEntry]) -> JournalAnalytics:
        total_pnl = sum(e.pnl for e in entries)
        avg_conf = sum(e.confidence for e in entries) / len(entries) if entries else 0
        tags: dict[str, int] = {}
        for entry in entries:
            for tag in entry.tags:
                tags[tag] = tags.get(tag, 0) + 1
        return JournalAnalytics(
            total_entries=len(entries),
            total_pnl=total_pnl,
            average_confidence=avg_conf,
            tags=tags,
        )
