from app.v500_alpha20_launcher_api_search.service import LauncherSwaggerAPISearchFacadeV500Alpha20

def test_v500_alpha20_facade_startup():
    assert LauncherSwaggerAPISearchFacadeV500Alpha20().startup_test()['ready'] is True
