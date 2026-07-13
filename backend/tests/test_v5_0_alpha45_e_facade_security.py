from app.v500_alpha45_runtime_enterprise.service import RuntimeEnterpriseFacadeV500Alpha45

def test_facade_security():
 r=RuntimeEnterpriseFacadeV500Alpha45().security(); assert r is not None
