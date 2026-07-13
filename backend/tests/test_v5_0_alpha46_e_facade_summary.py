from app.v500_alpha46_desktop_foundation.service import DesktopFoundationFacadeV500Alpha46

def test_facade_summary():
 r=DesktopFoundationFacadeV500Alpha46().summary(); assert r is not None
