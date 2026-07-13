from app.platform_core.exchange_layer.safety import ExchangeSafetyContract

def test_v500_alpha38_a_can_connect(): assert ExchangeSafetyContract().can_connect_real()['allowed'] is False