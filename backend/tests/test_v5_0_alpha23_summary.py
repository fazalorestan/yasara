from app.v500_alpha23_risk_engine.models import RiskEngineSummaryV500Alpha23

def test_v500_alpha23_summary():
    s=RiskEngineSummaryV500Alpha23(); assert s.ready is True; assert s.live_execution_enabled is False
