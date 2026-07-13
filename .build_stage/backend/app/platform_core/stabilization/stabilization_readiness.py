from app.platform_core.stabilization.technical_debt_report import technical_debt_report_service

class StabilizationReadinessGate:
    def run(self):
        report = technical_debt_report_service.report()
        ready = (
            report["ready"]
            and report["stabilization_only"]
            and report["adds_new_feature"] is False
            and report["refactor_guard"]["backward_compatibility_required"]
            and report["config_security"]["hardcoded_api_keys_allowed"] is False
            and report["backup_migration"]["auto_backup_before_update_required"]
            and report["commercial_execution_engine_enabled"] is False
            and report["commercial_api_key_required"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "stabilization_only": report["stabilization_only"],
                "adds_new_feature": report["adds_new_feature"],
                "backward_compatibility_required": report["refactor_guard"]["backward_compatibility_required"],
                "plugin_based_required": report["plugin_boundary"]["plugin_based_required"],
                "hardcoded_api_keys_allowed": report["config_security"]["hardcoded_api_keys_allowed"],
                "auto_backup_required": report["backup_migration"]["auto_backup_before_update_required"],
                "commercial_execution_engine_enabled": False,
                "commercial_api_key_required": False,
                "real_execution_enabled": False,
                "real_broker_connection_enabled": False,
            },
        }

stabilization_readiness_gate = StabilizationReadinessGate()
