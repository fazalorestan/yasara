from app.platform_core.live_data_pipeline.history_buffer import LiveDataHistoryBuffer

def test_v500_alpha39_d_history(): assert LiveDataHistoryBuffer().append(limit=3)['count']==3
