from app.v500_alpha47_production_readiness.service import ProductionReadinessFacadeV500Alpha47

def test_no_packaging_yet(): assert ProductionReadinessFacadeV500Alpha47().summary().packaging_enabled is False
