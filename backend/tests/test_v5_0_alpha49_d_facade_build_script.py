from app.v500_alpha49_windows_portable_build.service import WindowsPortableBuildFacadeV500Alpha49

def test_facade_build_script():
 assert WindowsPortableBuildFacadeV500Alpha49().build_script() is not None
