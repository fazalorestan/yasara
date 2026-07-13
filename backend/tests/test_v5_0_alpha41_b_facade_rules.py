from app.v500_alpha41_strategy_scoring.service import StrategyScoringFacadeV500Alpha41

def test_v500_alpha41_b_facade_rules():
 r=StrategyScoringFacadeV500Alpha41().rules(); assert r is not None
