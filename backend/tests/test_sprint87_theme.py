from app.desktop_ui_v1.theme import ThemeServiceV1

def test_theme_light():
    theme = ThemeServiceV1().get("light")
    assert theme.mode == "light"
    assert theme.background == "#FFFFFF"
