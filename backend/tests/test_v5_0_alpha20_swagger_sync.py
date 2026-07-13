from app.platform_core.api_search.swagger_sync import SwaggerSyncContract

def test_v500_alpha20_swagger_sync():
    s=SwaggerSyncContract().expected(); assert s['docs_url']=='/docs'; assert s['expected_endpoint_count'] >= 6
