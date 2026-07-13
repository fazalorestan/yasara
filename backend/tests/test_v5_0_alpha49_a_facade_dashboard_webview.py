from app.v500_alpha49_native_desktop.service import NativeDesktopApplicationFacadeV500Alpha49

def test_facade_dashboard_webview():
 assert NativeDesktopApplicationFacadeV500Alpha49().dashboard_webview() is not None
