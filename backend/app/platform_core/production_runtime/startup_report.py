from app.platform_core.production_runtime.boot_contract import runtime_boot_contract_service
from app.platform_core.production_runtime.runtime_core import runtime_core_service
from app.platform_core.production_runtime.runtime_mode import runtime_mode_resolver

class RuntimeStartupReportService:
    def report(self):
        return {
            "ready": True,
            "core": runtime_core_service.status(),
            "boot_contract": runtime_boot_contract_service.contract(),
            "dry_boot": runtime_boot_contract_service.dry_boot(),
            "personal_mode": runtime_mode_resolver.resolve("personal"),
            "commercial_mode": runtime_mode_resolver.resolve("commercial"),
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

runtime_startup_report_service = RuntimeStartupReportService()
RuntimeStartupReport = RuntimeStartupReportService
runtime_startup_report = runtime_startup_report_service
