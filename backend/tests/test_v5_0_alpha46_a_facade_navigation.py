from app.v500_alpha46_desktop_host.service import DesktopHostFacadeV500Alpha46

def test_facade_navigation():
 r=DesktopHostFacadeV500Alpha46().navigation(); assert r is not None
