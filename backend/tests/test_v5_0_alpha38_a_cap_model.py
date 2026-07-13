from app.platform_core.exchange_layer.models import ExchangeCapability

def test_v500_alpha38_a_cap_model(): assert ExchangeCapability('e').spot is True