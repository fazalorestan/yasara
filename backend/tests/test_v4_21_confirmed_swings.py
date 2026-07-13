from app.v421_market_structure_pro.detectors import confirmed_swings

def test_v421_confirmed_swings():
    candles = [
        {"high": 10, "low": 5, "close": 7},
        {"high": 12, "low": 6, "close": 8},
        {"high": 16, "low": 7, "close": 10},
        {"high": 12, "low": 4, "close": 6},
        {"high": 11, "low": 6, "close": 7},
    ]
    swings = confirmed_swings(candles, 1, 1)
    assert swings["count"] >= 2
    assert swings["highs"]
    assert swings["lows"]
