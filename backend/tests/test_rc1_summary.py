from app.rc1_v1.rc_summary import RC1SummaryBuilderV1

def test_rc1_summary():
    summary = RC1SummaryBuilderV1().build()
    assert summary.ready is True
    assert summary.version == "1.0.0-rc1"
