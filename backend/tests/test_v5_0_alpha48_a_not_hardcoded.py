from app.v500_alpha48_windows_app.service import WindowsAppBootstrapFacadeV500Alpha48

def test_not_hardcoded(): assert WindowsAppBootstrapFacadeV500Alpha48().report()['hardcoded_dashboard'] is False
