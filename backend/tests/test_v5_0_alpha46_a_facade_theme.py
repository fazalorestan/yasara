from app.v500_alpha46_desktop_host.service import DesktopHostFacadeV500Alpha46

def test_facade_theme():
 r=DesktopHostFacadeV500Alpha46().theme(); assert r is not None
