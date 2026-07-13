from app.v500_alpha30_replay_engine.models import ReplayEngineSummaryV500Alpha30

def test_v500_alpha30_summary():
    s=ReplayEngineSummaryV500Alpha30(); assert s.ready is True; assert s.real_execution_enabled is False
