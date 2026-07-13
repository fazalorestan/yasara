from app.v500_alpha28_alert_engine.service import AlertEngineFacadeV500Alpha28

def test_v500_alpha28_facade_contract(): assert AlertEngineFacadeV500Alpha28().contract()['delivery_enabled'] is False
