from app.platform_core.execution_engine.order_router_contract import OrderRouterContractService

def test_v500_alpha42_b_dry_route(): assert OrderRouterContractService().dry_route()['executed'] is False
