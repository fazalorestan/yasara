from app.platform_core.project_intelligence.pic_enterprise_report import pic_enterprise_report_service

class PICEnterpriseReadinessGate:
    def run(self):
        report = pic_enterprise_report_service.report()
        ready = (
            report["ready"]
            and report["automation_contract"]["auto_update_enabled"]
            and report["test_hook"]["enabled"]
            and report["build_hook"]["enabled"]
            and report["run_hook"]["enabled"]
            and report["package_manifest"]["sprint_complete"]
            and report["hardcoded_dashboard"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "enterprise_report_ready": report["ready"],
                "automation_enabled": report["automation_contract"]["auto_update_enabled"],
                "test_hook_enabled": report["test_hook"]["enabled"],
                "build_hook_enabled": report["build_hook"]["enabled"],
                "run_hook_enabled": report["run_hook"]["enabled"],
                "sprint_complete": report["package_manifest"]["sprint_complete"],
                "hardcoded_dashboard": False,
            },
        }

pic_enterprise_readiness_gate = PICEnterpriseReadinessGate()
