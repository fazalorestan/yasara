from app.platform_core.indicators.release_gate.checkpoint import indicator_plugin_expansion_checkpoint
from app.platform_core.indicators.release_gate.gate import indicator_platform_1000_test_gate
from app.platform_core.indicators.release_gate.rc_contract import indicator_release_candidate_contract
from app.platform_core.indicators.release_gate.regression import indicator_regression_safety_summary
from app.platform_core.indicators.release_gate.stability import indicator_alpha_stability_report
from app.v500_alpha5_indicator_release_gate.models import IndicatorReleaseGateSummaryV500Alpha5

class IndicatorReleaseGateFacadeV500Alpha5:
    def summary(self):
        return IndicatorReleaseGateSummaryV500Alpha5()

    def gate(self):
        return indicator_platform_1000_test_gate.run()

    def stability(self):
        return indicator_alpha_stability_report.report()

    def regression(self):
        return indicator_regression_safety_summary.summary()

    def checkpoint(self):
        return indicator_plugin_expansion_checkpoint.checkpoint()

    def rc_contract(self):
        return indicator_release_candidate_contract.contract()

    def full_report(self):
        gate = self.gate()
        return {
            "ready": gate["ready"],
            "gate": gate,
            "stability": self.stability(),
            "regression": self.regression(),
            "checkpoint": self.checkpoint(),
            "release_candidate": self.rc_contract(),
            "execution_allowed": False,
        }
