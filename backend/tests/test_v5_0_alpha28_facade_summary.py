from app.v500_alpha28_alert_engine.service import AlertEngineFacadeV500Alpha28

def test_v500_alpha28_facade_summary(): assert AlertEngineFacadeV500Alpha28().summary().ready is True
