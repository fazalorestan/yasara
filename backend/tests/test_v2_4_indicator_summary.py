from app.v24_indicator_signal.service import IndicatorSignalServiceV24

def test_indicator_summary():
    s = IndicatorSignalServiceV24().summary()
    assert s.operational_progress_percent == 93
    assert s.remaining_to_full_operational_percent == 7
