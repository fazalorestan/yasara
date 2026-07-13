from app.v500_alpha47_production_readiness.service import ProductionReadinessFacadeV500Alpha47

def test_commercial_no_api_key(): assert ProductionReadinessFacadeV500Alpha47().report()['commercial_api_key_required'] is False
