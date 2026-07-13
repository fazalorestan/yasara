from app.v500_alpha45_runtime_lifecycle.service import RuntimeLifecycleFacadeV500Alpha45

def test_facade_event_bus():
 r=RuntimeLifecycleFacadeV500Alpha45().event_bus(); assert r is not None
