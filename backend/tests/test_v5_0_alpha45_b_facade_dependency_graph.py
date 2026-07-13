from app.v500_alpha45_runtime_services.service import RuntimeServicesFacadeV500Alpha45

def test_facade_dependency_graph():
 r=RuntimeServicesFacadeV500Alpha45().dependency_graph(); assert r is not None
