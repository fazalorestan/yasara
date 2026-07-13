from app.v500_alpha20_launcher_api_search.models import LauncherSwaggerAPISearchSummaryV500Alpha20

def test_v500_alpha20_summary():
    s=LauncherSwaggerAPISearchSummaryV500Alpha20(); assert s.ready is True; assert s.api_search is True
