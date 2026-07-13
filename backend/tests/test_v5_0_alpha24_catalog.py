from app.platform_core.runtime_api_smoke.catalog import RuntimeEndpointCatalog

def test_v500_alpha24_catalog(): assert len(RuntimeEndpointCatalog().endpoints()) >= 6
