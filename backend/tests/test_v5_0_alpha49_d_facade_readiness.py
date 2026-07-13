from app.v500_alpha49_windows_portable_build.service import WindowsPortableBuildFacadeV500Alpha49

def test_facade_readiness():
 assert WindowsPortableBuildFacadeV500Alpha49().readiness() is not None
