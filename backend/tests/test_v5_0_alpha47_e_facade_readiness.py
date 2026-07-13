from app.v500_alpha47_production_readiness.service import ProductionReadinessFacadeV500Alpha47

def test_facade_readiness():
 r=ProductionReadinessFacadeV500Alpha47().readiness(); assert r is not None
