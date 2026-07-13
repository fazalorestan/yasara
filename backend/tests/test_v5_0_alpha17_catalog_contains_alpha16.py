from app.platform_core.api_health.catalog import APIEndpointCatalog

def test_v500_alpha17_catalog_contains_alpha16():
    paths = [e['path'] for e in APIEndpointCatalog().endpoints()]
    assert '/api/v1/v5-0-alpha-16/exchange-connector/summary' in paths
