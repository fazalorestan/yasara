from app.platform_core.project_intelligence.dashboard_layout_contract import DashboardLayoutContractService

def test_layout(): assert 'project_progress' in DashboardLayoutContractService().layout()['sections']
