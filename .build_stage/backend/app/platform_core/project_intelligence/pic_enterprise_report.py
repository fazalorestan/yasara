from app.platform_core.project_intelligence.dashboard_automation_contract import dashboard_automation_contract_service
from app.platform_core.project_intelligence.test_hook_contract import test_hook_contract_service
from app.platform_core.project_intelligence.build_hook_contract import build_hook_contract_service
from app.platform_core.project_intelligence.run_hook_contract import run_hook_contract_service
from app.platform_core.project_intelligence.sprint_package_manifest import sprint_package_manifest_service
from app.platform_core.project_intelligence.desktop_dashboard_report import desktop_dashboard_report_service
from app.platform_core.project_intelligence.state_sync_report import state_sync_report_service
from app.platform_core.project_intelligence.dashboard_report import live_dashboard_report_service
from app.platform_core.project_intelligence.pic_report import project_intelligence_report_service

class PICEnterpriseReportService:
    def report(self):
        return {
            "ready": True,
            "sprint": "v5.0-alpha.44",
            "name": "Project Intelligence Center",
            "packages": ["A-Core-State", "B-Live-Dashboard", "C-Build-Intelligence", "D-Desktop-Shell", "E-Automation"],
            "core_report": project_intelligence_report_service.report(),
            "live_dashboard_report": live_dashboard_report_service.report(),
            "state_sync_report": state_sync_report_service.report(),
            "desktop_dashboard_report": desktop_dashboard_report_service.report(),
            "automation_contract": dashboard_automation_contract_service.contract(),
            "test_hook": test_hook_contract_service.hook(),
            "build_hook": build_hook_contract_service.hook(),
            "run_hook": run_hook_contract_service.hook(),
            "package_manifest": sprint_package_manifest_service.manifest(),
            "hardcoded_dashboard": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
        }

pic_enterprise_report_service = PICEnterpriseReportService()

# Backward Compatibility
PICEnterpriseReport = PICEnterpriseReportService
pic_enterprise_report = pic_enterprise_report_service
