from app.v500_alpha45_runtime_lifecycle.service import RuntimeLifecycleFacadeV500Alpha45

def test_facade_restart():
 r=RuntimeLifecycleFacadeV500Alpha45().restart(); assert r is not None
