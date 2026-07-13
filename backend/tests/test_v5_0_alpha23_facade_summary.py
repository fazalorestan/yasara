from app.v500_alpha23_risk_engine.service import RiskEngineFacadeV500Alpha23

def test_v500_alpha23_facade_summary(): assert RiskEngineFacadeV500Alpha23().summary().ready is True
