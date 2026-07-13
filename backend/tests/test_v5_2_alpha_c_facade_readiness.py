from app.v52_alpha_windows_spec_fix.service import WindowsSpecOutputFixFacadeV52Alpha

def test_facade_readiness(): assert WindowsSpecOutputFixFacadeV52Alpha().readiness() is not None
