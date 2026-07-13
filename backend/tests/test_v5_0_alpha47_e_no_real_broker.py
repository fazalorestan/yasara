from app.v500_alpha47_production_readiness.service import ProductionReadinessFacadeV500Alpha47

def test_no_real_broker(): assert ProductionReadinessFacadeV500Alpha47().report()['real_broker_connection_enabled'] is False
