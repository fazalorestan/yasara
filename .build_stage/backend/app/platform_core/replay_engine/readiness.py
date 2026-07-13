from app.platform_core.replay_engine.service import replay_engine_foundation_service

class ReplayEngineReadinessGate:
    def run(self):
        session = replay_engine_foundation_service.session()
        timeline = replay_engine_foundation_service.timeline()
        playback = replay_engine_foundation_service.play_contract()
        link = replay_engine_foundation_service.backtest_link()
        ready = session["ready"] and timeline["ready"] and playback["ready"] and link["ready"]
        return {"ready": ready, "checks": {"session_ready": session["ready"], "timeline_ready": timeline["ready"], "playback_ready": playback["ready"], "backtest_link_ready": link["ready"], "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}

replay_engine_readiness_gate = ReplayEngineReadinessGate()
