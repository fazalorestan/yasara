from app.platform_core.project_intelligence.dashboard_automation_contract import DashboardAutomationContractService

def test_automation(): assert DashboardAutomationContractService().contract()['auto_update_enabled'] is True
