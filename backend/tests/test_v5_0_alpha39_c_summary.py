from app.v500_alpha39_live_stream_manager.models import LiveStreamManagerSummaryV500Alpha39

def test_v500_alpha39_c_summary():
 s=LiveStreamManagerSummaryV500Alpha39(); assert s.ready and s.test_pack_size==60
