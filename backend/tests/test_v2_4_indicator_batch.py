from app.v24_indicator_signal.service import IndicatorSignalServiceV24

def test_indicator_batch():
    batch = IndicatorSignalServiceV24().batch()
    assert batch["ready"] is True
    assert len(batch["items"]) >= 4
    assert batch["live_trading_enabled"] is False
