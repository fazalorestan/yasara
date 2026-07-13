from app.platform_core.router_auto_registration.importer import RouteModuleImporter

def test_v500_alpha30_1_importer_bad(): assert RouteModuleImporter().inspect('app.nope')['ready'] is False
