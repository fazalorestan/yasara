from app.platform_core.broker_layer.order_adapter_contract import BrokerOrderAdapterContractService

def test_v500_alpha43_c_adapter(): assert BrokerOrderAdapterContractService().contract()['real_order_submit_enabled'] is False
