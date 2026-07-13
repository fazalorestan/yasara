from app.platform_core.auto_router_registry.service import AutoRouterRegistryService

def test_v500_alpha34_0_service_contract(): assert AutoRouterRegistryService().contract()['manual_router_patch_required_after_this'] is False