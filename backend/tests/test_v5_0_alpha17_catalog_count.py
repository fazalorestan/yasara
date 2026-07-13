from app.platform_core.api_health.catalog import APIEndpointCatalog

def test_v500_alpha17_catalog_count():
    assert len(APIEndpointCatalog().endpoints()) >= 9
