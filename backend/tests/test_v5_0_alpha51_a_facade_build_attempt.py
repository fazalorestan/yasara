from app.v500_alpha51_exe_smoke_build.service import WindowsExeSmokeBuildFacadeV500Alpha51

def test_facade_build_attempt(): assert WindowsExeSmokeBuildFacadeV500Alpha51().build_attempt() is not None
