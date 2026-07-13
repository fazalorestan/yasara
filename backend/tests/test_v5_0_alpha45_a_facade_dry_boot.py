from app.v500_alpha45_runtime_core.service import RuntimeCoreFacadeV500Alpha45

def test_facade_dry_boot():
 r=RuntimeCoreFacadeV500Alpha45().dry_boot(); assert r is not None
