from app.platform_core.contracts.base import BaseContract

class ExecutionContractV426(BaseContract):
    contract_name = "execution"

    def execute(self, approved_payload: dict):
        raise NotImplementedError("Execution plugins must implement execute(approved_payload)")
