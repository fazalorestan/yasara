from app.v425_policy_gate.execution_contract import ExecutionIsolationGuardV425
from app.v425_policy_gate.gate import PluginPolicyGateV425
from app.v425_policy_gate.models import PolicyContextV425, PolicyGateSummaryV425, PolicyRequirementV425

class PolicyGateServiceV425:
    def __init__(self):
        self.gate = PluginPolicyGateV425()
        self.guard = ExecutionIsolationGuardV425()

    def summary(self):
        return PolicyGateSummaryV425()

    def evaluate(self, context: PolicyContextV425 | None = None, requirement: PolicyRequirementV425 | None = None):
        return self.gate.evaluate(context or PolicyContextV425(), requirement or PolicyRequirementV425())

    def execution_contract(self):
        return self.guard.execution_contract()

    def validate_analysis_payload(self, payload: dict | None = None):
        return self.guard.validate_analysis_payload(payload or {})
