from app.platform_core.exchange_layer.symbols import ExchangeSymbolRegistryService

def test_v500_alpha38_b_symbols(): assert 'BTCUSDT' in ExchangeSymbolRegistryService().symbols()['symbols']