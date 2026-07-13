from app.v500_alpha46_desktop_host.service import DesktopHostFacadeV500Alpha46

def test_facade_health():
 r=DesktopHostFacadeV500Alpha46().health(); assert r is not None
