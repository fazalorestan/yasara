from app.v500_alpha42_order_routing.service import OrderRoutingFacadeV500Alpha42

def test_v500_alpha42_b_facade_pre_trade_checks():
 r=OrderRoutingFacadeV500Alpha42().pre_trade_checks(); assert r is not None
