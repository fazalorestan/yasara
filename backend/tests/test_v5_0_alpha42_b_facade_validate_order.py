from app.v500_alpha42_order_routing.service import OrderRoutingFacadeV500Alpha42

def test_v500_alpha42_b_facade_validate_order():
 r=OrderRoutingFacadeV500Alpha42().validate_order(); assert r is not None
