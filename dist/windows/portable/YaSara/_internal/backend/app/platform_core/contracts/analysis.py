from app.platform_core.contracts.base import BaseContract

class AnalysisContract(BaseContract):
    contract_name = "analysis"

    def analyze(self, payload: dict):
        raise NotImplementedError("Analysis plugins must implement analyze(payload)")
