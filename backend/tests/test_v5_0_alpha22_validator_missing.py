from app.platform_core.broker.validation import BrokerOrderValidator

def test_v500_alpha22_validator_missing():
    assert BrokerOrderValidator().validate({'symbol':'BTCUSDT'})['valid'] is False
