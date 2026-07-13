from app.platform_core.live_data_pipeline.stream_session import LiveStreamSessionManager

def test_v500_alpha39_c_close_session(): assert LiveStreamSessionManager().close('s')['state']=='closed'
