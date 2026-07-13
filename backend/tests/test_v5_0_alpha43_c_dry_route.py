from app.platform_core.broker_layer.dry_broker_router import DryBrokerRouterService

def test_v500_alpha43_c_dry_route(): assert DryBrokerRouterService().route()['routed'] is True
