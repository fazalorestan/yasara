from app.platform_core.broker_layer.orders import BrokerOrderContractService

def test_v500_alpha37_b_normalize(): assert BrokerOrderContractService().normalize({'symbol':'btcusdt','side':'BUY','quantity':1})['order']['symbol']=='BTCUSDT'