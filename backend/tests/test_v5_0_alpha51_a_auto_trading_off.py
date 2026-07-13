from app.v500_alpha51_exe_smoke_build.service import WindowsExeSmokeBuildFacadeV500Alpha51

def test_auto_trading_off(): assert WindowsExeSmokeBuildFacadeV500Alpha51().summary().auto_trading_enabled is False
