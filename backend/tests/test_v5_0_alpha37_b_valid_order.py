from app.platform_core.broker_layer.order_validation import BrokerOrderValidationService

def test_v500_alpha37_b_valid_order(): assert BrokerOrderValidationService().validate({'symbol':'BTCUSDT','side':'buy','type':'market','quantity':1})['valid'] is True