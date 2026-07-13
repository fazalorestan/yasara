from app.platform_core.live_data_pipeline.stream_heartbeat import LiveStreamHeartbeat

def test_v500_alpha39_c_heartbeat(): assert LiveStreamHeartbeat().ping()['alive'] is True
