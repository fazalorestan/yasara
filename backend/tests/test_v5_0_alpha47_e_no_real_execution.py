from app.v500_alpha47_production_readiness.service import ProductionReadinessFacadeV500Alpha47

def test_no_real_execution(): assert ProductionReadinessFacadeV500Alpha47().report()['real_execution_enabled'] is False
