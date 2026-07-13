from app.platform_core.broker_layer.order_adapter_contract import BrokerOrderAdapterContractService

def test_v500_alpha43_c_dry_submit(): assert BrokerOrderAdapterContractService().dry_submit()['paper_submitted'] is True
