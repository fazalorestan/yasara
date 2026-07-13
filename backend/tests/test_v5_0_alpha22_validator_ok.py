from app.platform_core.broker.validation import BrokerOrderValidator

def test_v500_alpha22_validator_ok():
    assert BrokerOrderValidator().validate({'symbol':'BTCUSDT','side':'buy','order_type':'market','quantity':1})['valid'] is True
