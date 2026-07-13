from app.v500_alpha44_live_dashboard.models import LiveDashboardSummaryV500Alpha44

def test_guard(): assert LiveDashboardSummaryV500Alpha44().ready is True
