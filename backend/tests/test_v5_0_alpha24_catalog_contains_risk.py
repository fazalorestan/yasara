from app.platform_core.runtime_api_smoke.catalog import RuntimeEndpointCatalog

def test_v500_alpha24_catalog_contains_risk(): assert '/api/v1/v5-0-alpha-23/risk-engine/contract' in [x['path'] for x in RuntimeEndpointCatalog().endpoints()]
