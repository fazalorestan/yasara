from app.v500_alpha47_production_readiness.service import ProductionReadinessFacadeV500Alpha47

def test_commercial_no_execution(): assert ProductionReadinessFacadeV500Alpha47().report()['commercial_execution_engine_enabled'] is False
