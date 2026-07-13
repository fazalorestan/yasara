from app.v500_alpha45_runtime_enterprise.service import RuntimeEnterpriseFacadeV500Alpha45

def test_facade_acceptance():
 r=RuntimeEnterpriseFacadeV500Alpha45().acceptance(); assert r is not None
