from app.platform_core.api_search.catalog import APISearchCatalog

def test_v500_alpha20_catalog_contains_alpha20():
    assert '/api/v1/v5-0-alpha-20/api-search/summary' in [i['path'] for i in APISearchCatalog().endpoints()]
