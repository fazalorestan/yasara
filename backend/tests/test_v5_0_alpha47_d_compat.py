from app.platform_core.build_dashboard.report import BuildDashboardIntegrationReport, build_dashboard_integration_report

def test_compat(): assert BuildDashboardIntegrationReport().report()['ready'] and build_dashboard_integration_report.report()['ready']
