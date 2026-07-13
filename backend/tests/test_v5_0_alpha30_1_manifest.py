from app.platform_core.router_auto_registration.manifest import RouterEndpointManifestContract

def test_v500_alpha30_1_manifest(): assert RouterEndpointManifestContract().build([{'module_name':'x','import_path':'a','ready':True}])['total']==1
