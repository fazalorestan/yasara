from app.platform_core.desktop_finalization.smoke_finalization import DesktopSmokeFinalization

def test_smoke(): assert DesktopSmokeFinalization().result()['smoke_finalized'] is True
