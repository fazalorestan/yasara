class ReplayCursorService:
    def move(self, cursor: int, total: int, step: int = 1):
        next_cursor = min(max(cursor + step, 0), max(total - 1, 0))
        return {"ready": True, "cursor": next_cursor, "total": total}

    def reset(self):
        return {"ready": True, "cursor": 0}

replay_cursor_service = ReplayCursorService()
