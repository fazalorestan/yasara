from app.platform_core.replay_engine.cursor import replay_cursor_service
from app.platform_core.replay_engine.speed import replay_speed_service
from app.platform_core.replay_engine.timeline import replay_timeline_service

class ReplayPlaybackService:
    def state(self, cursor: int = 0, playing: bool = False, speed: float = 1.0):
        timeline = replay_timeline_service.build()
        return {"ready": True, "session_id": "replay_demo", "cursor": cursor, "total_events": timeline["total_events"], "playing": playing, "speed": speed}

    def step_forward(self, cursor: int = 0):
        timeline = replay_timeline_service.build()
        return replay_cursor_service.move(cursor, timeline["total_events"], 1)

    def play_contract(self, speed: float = 1.0):
        speed_check = replay_speed_service.set_speed(speed)
        return {"ready": speed_check["ready"], "playing": speed_check["ready"], "speed": speed_check["speed"], "live_execution": False, "auto_trading": False}

replay_playback_service = ReplayPlaybackService()
