from app.platform_core.api_search.search import APIEndpointSearchService

def test_v500_alpha20_search_missing():
    r=APIEndpointSearchService().find('not-existing'); assert r['ready'] is True; assert r['count'] == 0
