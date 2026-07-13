from app.desktop_ui_v1.heatmap import HeatmapBuilderV1

def test_heatmap_intensity():
    cells = HeatmapBuilderV1().build_change_heatmap({"BTC": 5, "ETH": -10})
    assert cells[1].intensity == 1
