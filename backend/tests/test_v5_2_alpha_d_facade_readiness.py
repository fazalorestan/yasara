from app.v52_alpha_native_launcher.service import NativeWindowsLauncherFacadeV52Alpha

def test_facade_readiness(): assert NativeWindowsLauncherFacadeV52Alpha().readiness() is not None
