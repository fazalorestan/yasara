from app.v500_alpha20_launcher_api_search.service import LauncherSwaggerAPISearchFacadeV500Alpha20

def test_v500_alpha20_facade_contract():
    c=LauncherSwaggerAPISearchFacadeV500Alpha20().contract(); assert c['ready'] is True; assert c['execution_allowed'] is False
