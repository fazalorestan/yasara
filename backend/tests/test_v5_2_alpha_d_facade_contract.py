from app.v52_alpha_native_launcher.service import NativeWindowsLauncherFacadeV52Alpha

def test_facade_contract(): assert NativeWindowsLauncherFacadeV52Alpha().contract() is not None
