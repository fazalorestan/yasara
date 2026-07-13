from app.v410_market_structure_sprint2.detectors import liquidity_sweep

def test_v410_sweep():
    s=liquidity_sweep([{'high':101,'low':95,'close':99}], {'buy_side_liquidity':[{'level':100}], 'sell_side_liquidity':[]}); assert s['detected'] is True
