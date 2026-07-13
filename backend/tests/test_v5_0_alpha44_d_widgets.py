from app.platform_core.project_intelligence.dashboard_widget_contracts import DashboardWidgetContractService

def test_widgets(): assert DashboardWidgetContractService().widgets()['count']==8
