from app.v500_alpha46_desktop_foundation.service import DesktopFoundationFacadeV500Alpha46

def test_facade_quality():
 r=DesktopFoundationFacadeV500Alpha46().quality(); assert r is not None
