from app.v500_alpha49_desktop_finalization.service import InternalDesktopBuildFinalizationFacadeV500Alpha49

def test_no_real_execution(): assert InternalDesktopBuildFinalizationFacadeV500Alpha49().report()['real_execution_enabled'] is False
