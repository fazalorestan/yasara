from app.platform_core.broker_layer.connection_status import BrokerConnectionStatusService

def test_v500_alpha43_d_connection(): assert BrokerConnectionStatusService().status()['connected'] is False
