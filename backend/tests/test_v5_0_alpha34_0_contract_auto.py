from app.platform_core.auto_router_registry.service import AutoRouterRegistryService

def test_v500_alpha34_0_contract_auto(): assert AutoRouterRegistryService().contract()['auto_trading_enabled'] is False