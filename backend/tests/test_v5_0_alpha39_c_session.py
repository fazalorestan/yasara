from app.platform_core.live_data_pipeline.stream_session import LiveStreamSessionManager

def test_v500_alpha39_c_session(): assert LiveStreamSessionManager().create()['state']=='created'
