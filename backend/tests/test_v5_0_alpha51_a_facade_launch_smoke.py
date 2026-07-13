from app.v500_alpha51_exe_smoke_build.service import WindowsExeSmokeBuildFacadeV500Alpha51

def test_facade_launch_smoke(): assert WindowsExeSmokeBuildFacadeV500Alpha51().launch_smoke() is not None
