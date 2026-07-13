from app.platform_core.strategy_engine.allocation_report import strategy_allocation_report
from app.platform_core.strategy_engine.enterprise.performance import strategy_enterprise_performance_gate
from app.platform_core.strategy_engine.enterprise.quality_score import strategy_enterprise_quality_score_service
from app.platform_core.strategy_engine.enterprise.report import strategy_enterprise_report_builder
from app.platform_core.strategy_engine.enterprise.runtime_acceptance import strategy_enterprise_runtime_acceptance
from app.platform_core.strategy_engine.enterprise.security import strategy_enterprise_security_gate
from app.platform_core.strategy_engine.report import strategy_core_report
from app.platform_core.strategy_engine.scoring_report import strategy_scoring_report
from app.platform_core.strategy_engine.simulation_report import strategy_simulation_report

class StrategyEnterpriseService:
    def security(self): return strategy_enterprise_security_gate.evaluate()
    def performance(self): return strategy_enterprise_performance_gate.evaluate()
    def quality_score(self):
        return strategy_enterprise_quality_score_service.calculate(
            security=self.security()["score"],
            performance=self.performance()["score"],
        )
    def runtime_acceptance(self): return strategy_enterprise_runtime_acceptance.contract()
    def final_report(self): return strategy_enterprise_report_builder.build()
    def final_status(self):
        core = strategy_core_report.report()
        scoring = strategy_scoring_report.report()
        allocation = strategy_allocation_report.report()
        simulation = strategy_simulation_report.report()
        quality = self.quality_score()
        return {
            "ready": core["ready"] and scoring["ready"] and allocation["ready"] and simulation["ready"] and quality["ready"],
            "core_ready": core["ready"],
            "scoring_ready": scoring["ready"],
            "allocation_ready": allocation["ready"],
            "simulation_ready": simulation["ready"],
            "quality_ready": quality["ready"],
            "quality_score": quality["overall"],
            "execution_allowed": False,
        }

strategy_enterprise_service = StrategyEnterpriseService()
