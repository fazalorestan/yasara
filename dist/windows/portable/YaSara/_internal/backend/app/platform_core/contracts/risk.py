from app.platform_core.contracts.base import BaseContract

class RiskContract(BaseContract):
    contract_name = "risk"

    def evaluate_risk(self, signal: dict):
        raise NotImplementedError("Risk plugins must implement evaluate_risk(signal)")
