from app.v500_alpha45_runtime_services.service import RuntimeServicesFacadeV500Alpha45

def test_facade_report():
 r=RuntimeServicesFacadeV500Alpha45().report(); assert r is not None
