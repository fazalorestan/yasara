from app.v410_market_structure_sprint2.detectors import liquidity_zones

def test_v410_liquidity_zones():
    z=liquidity_zones({'highs':[{'price':100},{'price':100.02}], 'lows':[{'price':90},{'price':90.01}]},0.08); assert 'equal_highs' in z; assert 'equal_lows' in z
