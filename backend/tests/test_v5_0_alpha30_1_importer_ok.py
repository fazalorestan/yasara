from app.platform_core.router_auto_registration.importer import RouteModuleImporter

def test_v500_alpha30_1_importer_ok(): assert RouteModuleImporter().inspect('app.api.v1.routes.v500_alpha30_replay_engine_v1')['has_router'] is True
