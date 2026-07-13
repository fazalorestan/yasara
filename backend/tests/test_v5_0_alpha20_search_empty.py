from app.platform_core.api_search.search import APIEndpointSearchService

def test_v500_alpha20_search_empty():
    r=APIEndpointSearchService().find(''); assert r['ready'] is True; assert r['count'] >= 6
