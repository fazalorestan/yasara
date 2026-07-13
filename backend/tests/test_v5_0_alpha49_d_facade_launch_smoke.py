from app.v500_alpha49_windows_portable_build.service import WindowsPortableBuildFacadeV500Alpha49

def test_facade_launch_smoke():
 assert WindowsPortableBuildFacadeV500Alpha49().launch_smoke() is not None
