from app.platform_core.exchange_layer.safety import ExchangeSafetyContract

def test_v500_alpha38_a_safety(): assert ExchangeSafetyContract().policy()['market_data_only'] is True