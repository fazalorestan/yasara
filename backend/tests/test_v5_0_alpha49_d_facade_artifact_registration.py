from app.v500_alpha49_windows_portable_build.service import WindowsPortableBuildFacadeV500Alpha49

def test_facade_artifact_registration():
 assert WindowsPortableBuildFacadeV500Alpha49().artifact_registration() is not None
