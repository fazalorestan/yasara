from app.v500_alpha45_runtime_core.service import RuntimeCoreFacadeV500Alpha45

def test_facade_startup_report():
 r=RuntimeCoreFacadeV500Alpha45().startup_report(); assert r is not None
