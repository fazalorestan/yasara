from app.v35_smart_money.detectors import detect_bos, detect_choch, detect_equal_high_low, detect_fvg, detect_imbalance, detect_liquidity_sweep, detect_order_block, premium_discount, score_smart_money

def test_v35_detectors():
    candles = [{"time":i, "open":100+i, "high":103+i, "low":98+i, "close":102+i, "volume":1000} for i in range(80)]
    bos = detect_bos(candles)
    choch = detect_choch(candles)
    sweep = detect_liquidity_sweep(candles)
    ob = detect_order_block(candles)
    fvg = detect_fvg(candles)
    imb = detect_imbalance(candles)
    eq = detect_equal_high_low(candles)
    pd = premium_discount(candles)
    score = score_smart_money(bos, choch, sweep, ob, fvg, pd)
    assert "detected" in bos
    assert "detected" in choch
    assert isinstance(fvg, list)
    assert isinstance(imb, list)
    assert "equal_highs" in eq
    assert pd["zone"] in ["premium", "discount", "equilibrium", "unknown"]
    assert 0 <= score["score"] <= 100
