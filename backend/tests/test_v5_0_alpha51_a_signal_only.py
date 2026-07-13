from app.v500_alpha51_exe_smoke_build.service import WindowsExeSmokeBuildFacadeV500Alpha51

def test_signal_only(): assert WindowsExeSmokeBuildFacadeV500Alpha51().summary().signal_only_mode is True
