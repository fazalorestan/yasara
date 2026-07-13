from app.v500_alpha45_runtime_lifecycle.service import RuntimeLifecycleFacadeV500Alpha45

def test_facade_session():
 r=RuntimeLifecycleFacadeV500Alpha45().session(); assert r is not None
