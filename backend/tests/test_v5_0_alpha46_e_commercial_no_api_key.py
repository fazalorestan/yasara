from app.v500_alpha46_desktop_foundation.service import DesktopFoundationFacadeV500Alpha46

def test_commercial_no_api_key(): assert DesktopFoundationFacadeV500Alpha46().report()["commercial_api_key_required"] is False
