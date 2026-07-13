from app.platform_core.production_runtime.dependency_graph import runtime_dependency_graph_service
from app.platform_core.production_runtime.service_health import runtime_service_health_contract
from app.platform_core.production_runtime.service_orchestrator import runtime_service_orchestrator
from app.platform_core.production_runtime.service_registry import runtime_service_registry
from app.platform_core.production_runtime.startup_order import runtime_startup_order_planner

class RuntimeServiceReportService:
    def report(self):
        return {
            "ready": True,
            "registry": runtime_service_registry.services(),
            "dependency_graph": runtime_dependency_graph_service.graph(),
            "startup_order": runtime_startup_order_planner.plan(),
            "health": runtime_service_health_contract.health(),
            "orchestration": runtime_service_orchestrator.orchestrate(),
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

runtime_service_report_service = RuntimeServiceReportService()
RuntimeServiceReport = RuntimeServiceReportService
runtime_service_report = runtime_service_report_service
