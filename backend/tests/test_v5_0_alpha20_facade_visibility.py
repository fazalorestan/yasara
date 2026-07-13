from app.v500_alpha20_launcher_api_search.service import LauncherSwaggerAPISearchFacadeV500Alpha20

def test_v500_alpha20_facade_visibility():
    assert LauncherSwaggerAPISearchFacadeV500Alpha20().visibility()['ready'] is True
