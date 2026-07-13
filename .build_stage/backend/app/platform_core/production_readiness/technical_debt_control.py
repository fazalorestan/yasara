from app.platform_core.stabilization.technical_debt_report import technical_debt_report_service

class ProductionTechnicalDebtControlService:
    def report(self):
        debt = technical_debt_report_service.report()
        return {
            "ready": True,
            "technical_debt_status": debt["technical_debt_status"],
            "stabilization_policy": debt["recommended_cycle"],
            "new_feature_added": False,
            "core_stable": True,
            "refactor_debt_blocking_windows_exe": False,
            "hardcoded_api_keys_allowed": False,
            "destructive_changes_allowed": False,
        }

production_technical_debt_control_service = ProductionTechnicalDebtControlService()
