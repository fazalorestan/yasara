from app.platform_core.production_runtime.event_bus_contract import runtime_event_bus_contract_service
from app.platform_core.production_runtime.lifecycle_manager import runtime_lifecycle_manager
from app.platform_core.production_runtime.restart_lifecycle import runtime_restart_lifecycle_service
from app.platform_core.production_runtime.session_manager import runtime_session_manager
from app.platform_core.production_runtime.shutdown_lifecycle import runtime_shutdown_lifecycle_service
from app.platform_core.production_runtime.startup_lifecycle import runtime_startup_lifecycle_service

class RuntimeLifecycleReportService:
    def report(self):
        return {
            "ready": True,
            "lifecycle": runtime_lifecycle_manager.lifecycle(),
            "startup": runtime_startup_lifecycle_service.startup(),
            "shutdown": runtime_shutdown_lifecycle_service.shutdown(),
            "restart": runtime_restart_lifecycle_service.restart(),
            "session": runtime_session_manager.session(),
            "event_bus": runtime_event_bus_contract_service.contract(),
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

runtime_lifecycle_report_service = RuntimeLifecycleReportService()
RuntimeLifecycleReport = RuntimeLifecycleReportService
runtime_lifecycle_report = runtime_lifecycle_report_service
