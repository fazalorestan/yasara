from app.v500_alpha45_runtime_enterprise.service import RuntimeEnterpriseFacadeV500Alpha45

def test_facade_report():
 r=RuntimeEnterpriseFacadeV500Alpha45().report(); assert r is not None
