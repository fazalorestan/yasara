from app.v412_smart_money_pro_sprint2.detectors import ob_fvg_confluence, premium_discount_entry
def test_v412_pd_confluence():
    p=premium_discount_entry({"zone":"discount"}, "bullish")
    c=ob_fvg_confluence([{"type":"bullish_order_block","low":99,"high":101}], [{"type":"bullish_fvg","from":100,"to":102}])
    assert p["aligned"] is True
    assert len(c) == 1
