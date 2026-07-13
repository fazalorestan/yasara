from app.platform_core.replay_engine.readiness import replay_engine_readiness_gate
from app.platform_core.replay_engine.service import replay_engine_foundation_service
from app.v500_alpha30_replay_engine.models import ReplayEngineSummaryV500Alpha30

class ReplayEngineFacadeV500Alpha30:
    def summary(self): return ReplayEngineSummaryV500Alpha30()
    def session(self): return replay_engine_foundation_service.session()
    def timeline(self): return replay_engine_foundation_service.timeline()
    def state(self): return replay_engine_foundation_service.state()
    def step_forward(self): return replay_engine_foundation_service.step_forward()
    def play_contract(self): return replay_engine_foundation_service.play_contract()
    def speed_contract(self): return replay_engine_foundation_service.speed_contract()
    def backtest_link(self): return replay_engine_foundation_service.backtest_link()
    def replay_summary(self): return replay_engine_foundation_service.replay_summary()
    def readiness(self): return replay_engine_readiness_gate.run()
    def contract(self): return {"ready": True, "replay_engine": "foundation_only", "requires_backtest_engine": True, "execution_allowed": False}
