from app.platform_core.exchange_layer.connection_state import ExchangeConnectionStateMachine

def test_v500_alpha38_c_state_initial(): assert ExchangeConnectionStateMachine().initial()['state']=='disconnected'