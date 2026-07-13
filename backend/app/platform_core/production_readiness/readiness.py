from app.platform_core.production_readiness.report import production_readiness_report_service

class ProductionReadinessGate:
    def run(self):
        report = production_readiness_report_service.report()
        ready = (
            report["ready"]
            and report["manifest"]["sprint_complete"]
            and report["architecture"]["architecture_stable"]
            and report["production_contract"]["windows_exe_handoff_ready"]
            and report["consolidation"]["consolidated"]
            and report["technical_debt"]["refactor_debt_blocking_windows_exe"] is False
            and report["windows_exe_handoff"]["ready"]
            and report["hardcoded_dashboard"] is False
            and report["commercial_execution_engine_enabled"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "sprint_complete": report["manifest"]["sprint_complete"],
                "architecture_stable": report["architecture"]["architecture_stable"],
                "windows_exe_handoff_ready": report["production_contract"]["windows_exe_handoff_ready"],
                "consolidated": report["consolidation"]["consolidated"],
                "technical_debt_blocking": report["technical_debt"]["refactor_debt_blocking_windows_exe"],
                "next_sprint_ready": report["next_sprint_ready"],
                "packaging_enabled": report["packaging_enabled"],
                "hardcoded_dashboard": False,
                "commercial_execution_engine_enabled": False,
                "commercial_api_key_required": False,
                "real_execution_enabled": False,
                "real_broker_connection_enabled": False,
            },
        }

production_readiness_gate = ProductionReadinessGate()
