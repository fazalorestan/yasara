from app.v500_alpha48_windows_app.service import WindowsAppBootstrapFacadeV500Alpha48

def test_facade_dashboard_host():
 r=WindowsAppBootstrapFacadeV500Alpha48().dashboard_host(); assert r is not None
