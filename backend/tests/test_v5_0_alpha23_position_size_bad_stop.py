from app.platform_core.risk_engine.position_size import PositionSizeCalculator

def test_v500_alpha23_position_size_bad_stop(): assert PositionSizeCalculator().calculate(10000,1,100,100)['reason']=='invalid_stop_distance'
