from app.v500_alpha45_runtime_core.service import RuntimeCoreFacadeV500Alpha45

def test_facade_safety():
 r=RuntimeCoreFacadeV500Alpha45().safety(); assert r is not None
