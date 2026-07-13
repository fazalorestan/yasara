from app.v500_alpha46_desktop_foundation.service import DesktopFoundationFacadeV500Alpha46

def test_facade_contract():
 r=DesktopFoundationFacadeV500Alpha46().contract(); assert r is not None
