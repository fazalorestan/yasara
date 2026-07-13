from app.platform_core.exchange_layer.health import ExchangeHealthService

def test_v500_alpha38_a_health(): assert ExchangeHealthService().health({'exchange_id':'e','enabled':True})['status']=='ok'