from app.v500_alpha47_production_readiness.service import ProductionReadinessFacadeV500Alpha47

def test_facade_report():
 r=ProductionReadinessFacadeV500Alpha47().report(); assert r is not None
