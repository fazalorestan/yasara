from app.platform_core.broker_layer.order_validation import BrokerOrderValidationService

def test_v500_alpha37_b_bad_price(): assert 'invalid_price' in BrokerOrderValidationService().validate({'symbol':'BTC','side':'buy','type':'limit','quantity':1,'price':0})['errors']