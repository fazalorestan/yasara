from app.platform_core.live_data_pipeline.stream_heartbeat import LiveStreamHeartbeat

def test_v500_alpha39_c_timeout(): assert LiveStreamHeartbeat().timeout_check(40000)['timed_out'] is True
