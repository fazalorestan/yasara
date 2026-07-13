from app.platform_core.clock import utc_now_iso

class ReplaySessionService:
    def create(self, symbol: str = "BTCUSDT", timeframe: str = "1h"):
        return {"ready": True, "session_id": "replay_demo", "symbol": symbol, "timeframe": timeframe, "speed": 1.0, "cursor": 0, "playing": False, "created_at": utc_now_iso()}

replay_session_service = ReplaySessionService()
