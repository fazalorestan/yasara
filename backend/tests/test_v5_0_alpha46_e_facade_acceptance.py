from app.v500_alpha46_desktop_foundation.service import DesktopFoundationFacadeV500Alpha46

def test_facade_acceptance():
 r=DesktopFoundationFacadeV500Alpha46().acceptance(); assert r is not None
