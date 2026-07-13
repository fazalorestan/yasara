from app.v500_alpha47_build_dashboard.service import BuildDashboardFacadeV500Alpha47

def test_facade_pipeline_status():
 r=BuildDashboardFacadeV500Alpha47().pipeline_status(); assert r is not None
