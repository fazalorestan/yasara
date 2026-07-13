from app.platform_core.broker_layer.account_report import broker_account_report_service
from app.platform_core.broker_layer.connectivity_report import broker_connectivity_report_service
from app.platform_core.broker_layer.enterprise.performance import broker_enterprise_performance_gate
from app.platform_core.broker_layer.enterprise.quality_score import broker_enterprise_quality_score_service
from app.platform_core.broker_layer.enterprise.report import broker_enterprise_report_builder
from app.platform_core.broker_layer.enterprise.runtime_acceptance import broker_enterprise_runtime_acceptance
from app.platform_core.broker_layer.enterprise.security import broker_enterprise_security_gate
from app.platform_core.broker_layer.service import broker_layer_core_service
class BrokerEnterpriseService:
    def security(self): return broker_enterprise_security_gate.evaluate()
    def performance(self): return broker_enterprise_performance_gate.evaluate()
    def quality_score(self): return broker_enterprise_quality_score_service.calculate(security=self.security()["score"], performance=self.performance()["score"])
    def runtime_acceptance(self): return broker_enterprise_runtime_acceptance.contract()
    def final_report(self): return broker_enterprise_report_builder.build()
    def final_status(self):
        core = broker_layer_core_service.status()
        orders = broker_account_report_service.report()
        connectivity = broker_connectivity_report_service.report()
        quality = self.quality_score()
        return {"ready": core["ready"] and orders["ready"] and connectivity["ready"] and quality["ready"], "core_ready": core["ready"], "orders_ready": orders["ready"], "connectivity_ready": connectivity["ready"], "quality_ready": quality["ready"], "quality_score": quality["overall"], "execution_allowed": False}
broker_enterprise_service = BrokerEnterpriseService()
