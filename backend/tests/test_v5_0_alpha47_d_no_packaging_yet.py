from app.v500_alpha47_build_dashboard.service import BuildDashboardFacadeV500Alpha47

def test_no_packaging_yet(): assert BuildDashboardFacadeV500Alpha47().summary().packaging_enabled is False
