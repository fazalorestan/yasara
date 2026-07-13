from app.platform_core.exchange_layer.streams import ExchangeStreamContractService

def test_v500_alpha38_c_stream_contract(): assert 'ticker' in ExchangeStreamContractService().stream_contract()['streams']