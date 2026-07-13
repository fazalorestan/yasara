from app.platform_core.broker_layer.connection_state import BrokerConnectionStateMachine

def test_v500_alpha37_c_state_initial(): assert BrokerConnectionStateMachine().initial()['state']=='disconnected'