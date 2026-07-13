from app.platform_core.indicators.readiness.e2e_contract import yasara_indicator_e2e_contract
from app.platform_core.indicators.readiness.gate import yasara_indicator_readiness_gate
from app.platform_core.indicators.readiness.safety import yasara_indicator_safety_report
from app.v449_indicator_final_readiness.models import IndicatorFinalReadinessSummaryV449

class IndicatorFinalReadinessFacadeV449:
    def summary(self):
        return IndicatorFinalReadinessSummaryV449()

    def gate(self):
        return yasara_indicator_readiness_gate.run()

    def e2e_contract(self):
        return yasara_indicator_e2e_contract.contract()

    def safety(self):
        return yasara_indicator_safety_report.report()

    def v5_readiness(self):
        gate = self.gate()
        safety = self.safety()
        return {
            "ready": gate["ready"] and safety["ready"],
            "indicator": "yasara",
            "score": gate["score"],
            "v5_plugin_ready": gate["v5_ready"] and safety["safe_for_v5_plugin_expansion"],
            "execution_allowed": False,
            "mode": "analysis_only",
        }
