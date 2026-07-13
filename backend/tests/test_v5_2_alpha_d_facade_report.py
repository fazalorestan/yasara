from app.v52_alpha_native_launcher.service import NativeWindowsLauncherFacadeV52Alpha

def test_facade_report(): assert NativeWindowsLauncherFacadeV52Alpha().report() is not None
