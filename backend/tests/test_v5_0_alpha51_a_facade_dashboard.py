from app.v500_alpha51_exe_smoke_build.service import WindowsExeSmokeBuildFacadeV500Alpha51

def test_facade_dashboard(): assert WindowsExeSmokeBuildFacadeV500Alpha51().dashboard() is not None
