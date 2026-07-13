from app.v421_market_structure_pro.detectors import chart_annotations

def test_v421_annotations():
    swings = {"highs": [{"index": 1, "time": 1, "price": 10}], "lows": [{"index": 2, "time": 2, "price": 5}]}
    events = [{"type": "BOS", "direction": "bullish", "index": 3, "time": 3, "level": 10, "label": "BOS Bullish"}]
    annotations = chart_annotations(swings, events, {"ranging": False})
    assert len(annotations) >= 3
