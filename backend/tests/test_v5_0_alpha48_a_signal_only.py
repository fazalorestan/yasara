from app.v500_alpha48_windows_app.service import WindowsAppBootstrapFacadeV500Alpha48

def test_signal_only(): assert WindowsAppBootstrapFacadeV500Alpha48().summary().signal_only_mode is True
