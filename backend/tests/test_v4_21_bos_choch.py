from app.v421_market_structure_pro.detectors import confirmed_swings, detect_bos_choch

def test_v421_bos_choch():
    candles = [
        {"high": 10, "low": 5, "close": 7},
        {"high": 12, "low": 6, "close": 8},
        {"high": 15, "low": 7, "close": 10},
        {"high": 12, "low": 4, "close": 6},
        {"high": 11, "low": 6, "close": 7},
        {"high": 18, "low": 8, "close": 17},
        {"high": 16, "low": 2, "close": 3},
    ]
    swings = confirmed_swings(candles, 1, 1)
    events = detect_bos_choch(candles, swings)
    assert isinstance(events, list)
    assert any(e["type"] in ["BOS", "CHoCH"] for e in events)
