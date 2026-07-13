class FillContractService:
    def contract(self):
        return {
            "ready": True,
            "interface": "fill_contract",
            "methods": ["record_fill", "validate_fill", "report"],
            "real_fill_enabled": False,
            "execution_allowed": False,
        }

    def simulated_fill(self):
        return {
            "ready": True,
            "filled": False,
            "fill_qty": 0.0,
            "avg_price": 0.0,
            "source": "simulated",
            "execution_allowed": False,
        }

fill_contract_service = FillContractService()
