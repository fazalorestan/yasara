from app.v52_alpha_windows_spec_fix.service import WindowsSpecOutputFixFacadeV52Alpha

def test_facade_contract(): assert WindowsSpecOutputFixFacadeV52Alpha().contract() is not None
