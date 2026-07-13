from app.platform_core.broker_layer.connection_state import BrokerConnectionStateMachine

def test_v500_alpha37_c_state_connect(): assert BrokerConnectionStateMachine().transition('disconnected','connect')['to']=='connecting'