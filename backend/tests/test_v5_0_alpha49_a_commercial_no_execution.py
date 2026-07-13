from app.v500_alpha49_native_desktop.service import NativeDesktopApplicationFacadeV500Alpha49

def test_commercial_no_execution(): assert NativeDesktopApplicationFacadeV500Alpha49().report()['commercial_execution_engine_enabled'] is False
