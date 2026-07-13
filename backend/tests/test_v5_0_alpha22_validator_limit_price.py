from app.platform_core.broker.validation import BrokerOrderValidator

def test_v500_alpha22_validator_limit_price():
    r=BrokerOrderValidator().validate({'symbol':'BTCUSDT','side':'buy','order_type':'limit','quantity':1}); assert 'missing_price_for_limit_order' in r['errors']
