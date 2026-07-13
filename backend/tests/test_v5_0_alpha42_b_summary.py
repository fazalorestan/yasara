from app.v500_alpha42_order_routing.models import OrderRoutingSummaryV500Alpha42

def test_v500_alpha42_b_summary():
 s=OrderRoutingSummaryV500Alpha42(); assert s.ready and s.test_pack_size==60
