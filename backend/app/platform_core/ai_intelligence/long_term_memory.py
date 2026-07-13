class AILongTermMemoryContract:
    def contract(self):
        return {
            "ready": True,
            "interface": "ai_long_term_memory_contract",
            "storage_mode": "contract_only",
            "semantic_search_enabled": False,
            "provider_owned": False,
            "yasara_owned": True,
        }

    def simulated_recall(self, query: str = "risk"):
        return {
            "ready": True,
            "query": query,
            "results": [{"key": "risk_policy", "value": "real execution disabled"}],
            "source": "simulated",
        }

ai_long_term_memory_contract = AILongTermMemoryContract()
