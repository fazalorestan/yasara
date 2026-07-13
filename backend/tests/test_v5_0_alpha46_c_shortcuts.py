from app.platform_core.desktop_app.shortcut_registry import DesktopShortcutRegistry

def test_shortcuts(): assert DesktopShortcutRegistry().shortcuts()['count']==3
