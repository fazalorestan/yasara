from app.platform_core.replay_engine.backtest_link import replay_backtest_link_service
from app.platform_core.replay_engine.playback import replay_playback_service
from app.platform_core.replay_engine.session import replay_session_service
from app.platform_core.replay_engine.timeline import replay_timeline_service

class ReplayEngineFoundationService:
    def session(self): return replay_session_service.create()
    def timeline(self): return replay_timeline_service.build()
    def state(self): return replay_playback_service.state()
    def step_forward(self): return replay_playback_service.step_forward(0)
    def play_contract(self): return replay_playback_service.play_contract(1.0)
    def speed_contract(self): return replay_playback_service.play_contract(2.0)
    def backtest_link(self): return replay_backtest_link_service.link()
    def replay_summary(self):
        timeline = self.timeline()
        return {"ready": True, "total_events": timeline["total_events"], "symbol": timeline["symbol"], "execution_allowed": False}

replay_engine_foundation_service = ReplayEngineFoundationService()
