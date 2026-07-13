from app.v500_alpha51_exe_smoke_build.service import WindowsExeSmokeBuildFacadeV500Alpha51

def test_commercial_no_api_key(): assert WindowsExeSmokeBuildFacadeV500Alpha51().report()['commercial_api_key_required'] is False
