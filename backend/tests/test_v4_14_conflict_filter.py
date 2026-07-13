from app.v414_ai_fusion.fusion import conflict_detection, weak_signal_filter
def test_v414_conflict_filter():
    c=conflict_detection([{"module":"a","bias":"bullish"},{"module":"b","bias":"bearish"}])
    assert c["has_conflict"] is True
    f=weak_signal_filter(50, 20, {"agreement_percent":30})
    assert f["filtered"] is True
