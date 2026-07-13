from app.v500_alpha45_runtime_core.service import RuntimeCoreFacadeV500Alpha45

def test_facade_core_status():
 r=RuntimeCoreFacadeV500Alpha45().core_status(); assert r is not None
