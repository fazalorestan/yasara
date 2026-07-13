from app.platform_core.native_desktop.entrypoint import NativeDesktopEntrypoint

def test_entrypoint(): assert NativeDesktopEntrypoint().specification()['launch_main_window'] is True
