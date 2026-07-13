from app.platform_core.broker_layer.order_validation import BrokerOrderValidationService

def test_v500_alpha37_b_bad_side(): assert 'invalid_side' in BrokerOrderValidationService().validate({'symbol':'BTC','side':'x','type':'market','quantity':1})['errors']