from app.platform_core.exchange_layer.session import ExchangeSessionManager

def test_v500_alpha38_c_session(): assert ExchangeSessionManager().create_session()['state']=='created'