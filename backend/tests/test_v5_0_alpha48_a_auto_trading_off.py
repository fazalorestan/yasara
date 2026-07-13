from app.v500_alpha48_windows_app.service import WindowsAppBootstrapFacadeV500Alpha48

def test_auto_trading_off(): assert WindowsAppBootstrapFacadeV500Alpha48().summary().auto_trading_enabled is False
