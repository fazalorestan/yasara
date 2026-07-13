from app.v500_alpha49_windows_portable_build.service import WindowsPortableBuildFacadeV500Alpha49

def test_commercial_no_api_key(): assert WindowsPortableBuildFacadeV500Alpha49().report()['commercial_api_key_required'] is False
