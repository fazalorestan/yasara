from app.platform_core.contracts.base import BaseContract

class SignalContract(BaseContract):
    contract_name = "signal"

    def generate_signal(self, analysis_result: dict):
        raise NotImplementedError("Signal plugins must implement generate_signal(analysis_result)")
