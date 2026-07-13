from app.v412_smart_money_pro_sprint2.detectors import liquidity_grab
def test_v412_liquidity_grab():
    candles=[{"high":99,"low":95,"close":99},{"high":101,"low":96,"close":99}]
    zones={"buy_side_liquidity":[{"level":100}], "sell_side_liquidity":[]}
    g=liquidity_grab(candles,zones)
    assert g["detected"] is True
