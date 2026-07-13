from app.v500_alpha51_exe_smoke_build.service import WindowsExeSmokeBuildFacadeV500Alpha51

def test_facade_contract(): assert WindowsExeSmokeBuildFacadeV500Alpha51().contract() is not None
