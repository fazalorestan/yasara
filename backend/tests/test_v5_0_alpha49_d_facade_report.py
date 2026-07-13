from app.v500_alpha49_windows_portable_build.service import WindowsPortableBuildFacadeV500Alpha49

def test_facade_report():
 assert WindowsPortableBuildFacadeV500Alpha49().report() is not None
