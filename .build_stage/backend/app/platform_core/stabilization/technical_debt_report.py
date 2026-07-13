from app.platform_core.stabilization.backup_migration_guard import backup_migration_guard_service
from app.platform_core.stabilization.config_security_guard import config_security_guard_service
from app.platform_core.stabilization.duplicate_detector import duplicate_detector_service
from app.platform_core.stabilization.patch_consolidation import patch_consolidation_service
from app.platform_core.stabilization.plugin_boundary_guard import plugin_boundary_guard_service
from app.platform_core.stabilization.refactor_guard import refactor_guard_service

class TechnicalDebtReportService:
    def report(self):
        return {
            "ready": True,
            "stabilization_only": True,
            "adds_new_feature": False,
            "patch_consolidation": patch_consolidation_service.summary(),
            "duplicate_detector": duplicate_detector_service.scan(),
            "refactor_guard": refactor_guard_service.policy(),
            "plugin_boundary": plugin_boundary_guard_service.policy(),
            "config_security": config_security_guard_service.policy(),
            "backup_migration": backup_migration_guard_service.policy(),
            "technical_debt_status": "controlled",
            "recommended_cycle": "3_development_sprints_then_1_stabilization_sprint",
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

technical_debt_report_service = TechnicalDebtReportService()
TechnicalDebtReport = TechnicalDebtReportService
technical_debt_report = technical_debt_report_service
