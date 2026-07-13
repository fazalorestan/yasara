from app.desktop_ui_v1.layout import LayoutBuilderV1

def test_layout_two_column():
    layout = LayoutBuilderV1().two_column()
    assert len(layout.items) == 3
    assert layout.items[1].panel_id == "chart"
