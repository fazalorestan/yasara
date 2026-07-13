from app.v500_alpha46_desktop_foundation.service import DesktopFoundationFacadeV500Alpha46

def test_facade_report():
 r=DesktopFoundationFacadeV500Alpha46().report(); assert r is not None
