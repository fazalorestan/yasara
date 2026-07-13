from app.platform_core.risk_engine.position_size import PositionSizeCalculator

def test_v500_alpha23_position_size_bad_equity(): assert PositionSizeCalculator().calculate(0,1,100,95)['reason']=='invalid_equity'
