from app.platform_core.broker_layer.orders import BrokerOrderContractService

def test_v500_alpha37_b_sample_order(): assert BrokerOrderContractService().sample_order()['symbol']=='BTCUSDT'