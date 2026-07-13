from app.platform_core.execution_engine.order_contract import OrderContractService

def test_v500_alpha42_a_order_contract(): assert OrderContractService().contract()['execution_allowed'] is False
