from app.platform_core.risk_engine.position_size import PositionSizeCalculator

def test_v500_alpha23_position_size_ok():
    r=PositionSizeCalculator().calculate(10000,1,100,95); assert r['ready'] is True; assert r['quantity'] == 20
