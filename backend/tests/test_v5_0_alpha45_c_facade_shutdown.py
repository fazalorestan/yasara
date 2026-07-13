from app.v500_alpha45_runtime_lifecycle.service import RuntimeLifecycleFacadeV500Alpha45

def test_facade_shutdown():
 r=RuntimeLifecycleFacadeV500Alpha45().shutdown(); assert r is not None
