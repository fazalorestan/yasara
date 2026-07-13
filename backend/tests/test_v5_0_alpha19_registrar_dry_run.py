from app.platform_core.api_routing.registration import SafeRouterRegistrar

def test_v500_alpha19_registrar_dry_run():
    r=SafeRouterRegistrar().dry_run([{'import_path':'app.api.v1.routes.v500_alpha18_exchange_sdk_v1'}]); assert r['ready'] is True
