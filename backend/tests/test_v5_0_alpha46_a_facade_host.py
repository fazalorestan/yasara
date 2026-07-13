from app.v500_alpha46_desktop_host.service import DesktopHostFacadeV500Alpha46

def test_facade_host():
 r=DesktopHostFacadeV500Alpha46().host(); assert r is not None
