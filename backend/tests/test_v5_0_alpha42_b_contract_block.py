from app.v500_alpha42_order_routing.service import OrderRoutingFacadeV500Alpha42

def test_v500_alpha42_b_contract_block(): assert OrderRoutingFacadeV500Alpha42().contract()['execution_allowed'] is False
