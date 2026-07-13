from app.platform_core.broker_layer.session import BrokerSessionManager

def test_v500_alpha37_c_session(): assert BrokerSessionManager().create_session()['state']=='created'