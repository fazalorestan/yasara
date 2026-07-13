class TradingJournalAIReviewerV46:
    def detect_mistakes(self, entry):
        mistakes = list(entry.get("mistake_tags", []))
        if entry.get("pnl", 0) < 0 and not mistakes:
            mistakes.append("loss_without_tagged_reason")
        if entry.get("emotion") in ["fear", "greed", "revenge"]:
            mistakes.append(f"emotion_{entry.get('emotion')}")
        if entry.get("quantity", 0) <= 0:
            mistakes.append("invalid_or_missing_quantity")
        return sorted(set(mistakes))

    def review(self, entry):
        mistakes = self.detect_mistakes(entry)
        pnl = entry.get("pnl", 0)
        score = 70
        if pnl > 0:
            score += 10
        if pnl < 0:
            score -= 15
        score -= min(len(mistakes) * 7, 35)
        score = max(0, min(100, score))

        lesson = "Trade followed acceptable journal discipline."
        if mistakes:
            lesson = "Review the mistake tags and reduce emotional or unplanned decisions."
        if pnl < 0 and "loss_without_tagged_reason" in mistakes:
            lesson = "Every losing trade must have a clear reason, setup invalidation, or execution note."

        return {
            "ready": True,
            "entry_id": entry.get("id"),
            "discipline_score": score,
            "mistakes": mistakes,
            "lesson": lesson,
            "performance_coach_hint": "Focus on consistency, risk control, and avoiding repeated mistake tags.",
            "real_order_execution_enabled": False,
        }
