from app.v500_alpha46_desktop_host.service import DesktopHostFacadeV500Alpha46

def test_facade_summary():
 r=DesktopHostFacadeV500Alpha46().summary(); assert r is not None
