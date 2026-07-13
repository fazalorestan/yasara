from app.platform_core.desktop_app.enterprise_acceptance import DesktopEnterpriseAcceptanceContract

def test_acceptance(): assert DesktopEnterpriseAcceptanceContract().contract()["auto_router_registry_required"] is True
