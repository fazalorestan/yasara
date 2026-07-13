from app.platform_core.execution_engine.order_router_contract import OrderRouterContractService

def test_v500_alpha42_b_router_contract(): assert OrderRouterContractService().contract()['execution_allowed'] is False
