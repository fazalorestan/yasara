from app.v500_alpha49_desktop_finalization.service import InternalDesktopBuildFinalizationFacadeV500Alpha49

def test_facade_contract():
 assert InternalDesktopBuildFinalizationFacadeV500Alpha49().contract() is not None
