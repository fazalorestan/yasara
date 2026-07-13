from app.v500_alpha42_order_routing.service import OrderRoutingFacadeV500Alpha42

def test_v500_alpha42_b_facade_dry_route():
 r=OrderRoutingFacadeV500Alpha42().dry_route(); assert r is not None
