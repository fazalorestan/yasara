from app.v500_alpha49_desktop_finalization.service import InternalDesktopBuildFinalizationFacadeV500Alpha49

def test_facade_report():
 assert InternalDesktopBuildFinalizationFacadeV500Alpha49().report() is not None
