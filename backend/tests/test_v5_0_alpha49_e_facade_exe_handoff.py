from app.v500_alpha49_desktop_finalization.service import InternalDesktopBuildFinalizationFacadeV500Alpha49

def test_facade_exe_handoff():
 assert InternalDesktopBuildFinalizationFacadeV500Alpha49().exe_handoff() is not None
