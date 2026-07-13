from app.platform_core.exchange_layer.session import ExchangeSessionManager

def test_v500_alpha38_c_close(): assert ExchangeSessionManager().close_session('s')['state']=='closed'