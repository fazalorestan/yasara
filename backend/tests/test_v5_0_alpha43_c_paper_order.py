from app.platform_core.broker_layer.paper_order_contract import BrokerPaperOrderContractService

def test_v500_alpha43_c_paper_order(): assert BrokerPaperOrderContractService().paper_order()['real_order'] is False
