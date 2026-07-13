from app.platform_core.api_routing.swagger import SwaggerVisibilityContract

def test_v500_alpha19_swagger():
    s=SwaggerVisibilityContract().expected_visibility(); assert s['docs_url']=='/docs'; assert s['api_prefix']=='/api/v1'
