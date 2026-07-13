from app.v500_alpha20_launcher_api_search.service import LauncherSwaggerAPISearchFacadeV500Alpha20

def test_v500_alpha20_facade_find():
    r=LauncherSwaggerAPISearchFacadeV500Alpha20().find('exchange-sdk'); assert r['ready'] is True; assert r['count'] >= 1
