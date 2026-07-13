from app.platform_core.auto_router_registry.service import AutoRouterRegistryService

def test_v500_alpha34_0_contract_real(): assert AutoRouterRegistryService().contract()['real_execution_enabled'] is False