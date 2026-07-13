from app.platform_core.windows_app.local_backend_connector import WindowsLocalBackendConnector

def test_backend(): assert WindowsLocalBackendConnector().connector()['external_network_required'] is False
