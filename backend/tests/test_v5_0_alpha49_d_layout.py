from app.platform_core.windows_portable_build.layout import WindowsPortableBuildLayout

def test_layout(): assert WindowsPortableBuildLayout().layout()['portable_mode'] is True
