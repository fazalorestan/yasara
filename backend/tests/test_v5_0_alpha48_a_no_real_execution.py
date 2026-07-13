from app.v500_alpha48_windows_app.service import WindowsAppBootstrapFacadeV500Alpha48

def test_no_real_execution(): assert WindowsAppBootstrapFacadeV500Alpha48().report()['real_execution_enabled'] is False
