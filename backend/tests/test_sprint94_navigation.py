from app.desktop_ui_v1.navigation import NavigationBuilderV1

def test_navigation_main():
    nav = NavigationBuilderV1().main()
    assert nav[0].route == "/dashboard"
