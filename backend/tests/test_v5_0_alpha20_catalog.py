from app.platform_core.api_search.catalog import APISearchCatalog

def test_v500_alpha20_catalog():
    assert len(APISearchCatalog().endpoints()) >= 6
