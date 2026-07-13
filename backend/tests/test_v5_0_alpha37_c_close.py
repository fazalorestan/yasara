from app.platform_core.broker_layer.session import BrokerSessionManager

def test_v500_alpha37_c_close(): assert BrokerSessionManager().close_session('s')['state']=='closed'