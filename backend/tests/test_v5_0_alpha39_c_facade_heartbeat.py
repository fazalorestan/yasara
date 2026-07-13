from app.v500_alpha39_live_stream_manager.service import LiveStreamManagerFacadeV500Alpha39

def test_v500_alpha39_c_facade_heartbeat():
 r=LiveStreamManagerFacadeV500Alpha39().heartbeat(); assert r is not None
