from app.v500_alpha45_runtime_services.service import RuntimeServicesFacadeV500Alpha45

def test_facade_services():
 r=RuntimeServicesFacadeV500Alpha45().services(); assert r is not None
