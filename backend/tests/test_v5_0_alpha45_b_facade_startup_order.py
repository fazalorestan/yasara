from app.v500_alpha45_runtime_services.service import RuntimeServicesFacadeV500Alpha45

def test_facade_startup_order():
 r=RuntimeServicesFacadeV500Alpha45().startup_order(); assert r is not None
