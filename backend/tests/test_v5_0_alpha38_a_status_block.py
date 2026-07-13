from app.platform_core.exchange_layer.service import ExchangeLayerCoreService

def test_v500_alpha38_a_status_block(): assert ExchangeLayerCoreService().status()['execution_allowed'] is False
