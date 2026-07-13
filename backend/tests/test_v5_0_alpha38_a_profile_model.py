from app.platform_core.exchange_layer.models import ExchangeProfile

def test_v500_alpha38_a_profile_model(): assert ExchangeProfile('e','Exchange').mode=='sandbox'