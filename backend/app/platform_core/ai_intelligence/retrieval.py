class AIRetrievalContractService:
    def retrieve(self, query: str = "market"):
        return {
            "ready": True,
            "query": query,
            "results": [
                {"source": "session_memory", "content": "simulated session context"},
                {"source": "long_term_memory", "content": "simulated long-term context"},
            ],
            "real_vector_db_connection": False,
        }

ai_retrieval_contract_service = AIRetrievalContractService()
