from app.v500_alpha51_exe_smoke_build.service import WindowsExeSmokeBuildFacadeV500Alpha51

def test_facade_exe_check(): assert WindowsExeSmokeBuildFacadeV500Alpha51().exe_check() is not None
