from app.platform_core.live_data_pipeline.history_buffer import LiveDataHistoryBuffer

def test_v500_alpha39_d_latest(): assert LiveDataHistoryBuffer().latest()['latest']['symbol']=='BTCUSDT'
