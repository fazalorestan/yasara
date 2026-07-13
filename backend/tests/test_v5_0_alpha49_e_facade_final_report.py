from app.v500_alpha49_desktop_finalization.service import InternalDesktopBuildFinalizationFacadeV500Alpha49

def test_facade_final_report():
 assert InternalDesktopBuildFinalizationFacadeV500Alpha49().final_report() is not None
