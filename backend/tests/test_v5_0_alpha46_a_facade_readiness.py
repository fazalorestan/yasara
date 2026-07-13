from app.v500_alpha46_desktop_host.service import DesktopHostFacadeV500Alpha46

def test_facade_readiness():
 r=DesktopHostFacadeV500Alpha46().readiness(); assert r is not None
