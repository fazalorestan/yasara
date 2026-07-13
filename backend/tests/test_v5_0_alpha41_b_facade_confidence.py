from app.v500_alpha41_strategy_scoring.service import StrategyScoringFacadeV500Alpha41

def test_v500_alpha41_b_facade_confidence():
 r=StrategyScoringFacadeV500Alpha41().confidence(); assert r is not None
