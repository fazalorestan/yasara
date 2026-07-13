from app.v500_alpha23_risk_engine.service import RiskEngineFacadeV500Alpha23

def test_v500_alpha23_facade_contract(): assert RiskEngineFacadeV500Alpha23().contract()['execution_allowed'] is False
