from datetime import datetime, timedelta, timezone
from app.market_data.application.sync_service import TIMEFRAME_SECONDS

def test_timeframe_seconds():
    assert TIMEFRAME_SECONDS["1m"] == 60
    assert TIMEFRAME_SECONDS["15m"] == 900
    assert TIMEFRAME_SECONDS["1h"] == 3600
