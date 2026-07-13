from app.v500_alpha47_production_readiness.service import ProductionReadinessFacadeV500Alpha47

def test_facade_windows_exe_handoff():
 r=ProductionReadinessFacadeV500Alpha47().windows_exe_handoff(); assert r is not None
