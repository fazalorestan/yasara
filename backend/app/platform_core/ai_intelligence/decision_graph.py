class AIDecisionGraphService:
    def graph(self):
        return {
            "ready": True,
            "nodes": [
                {"id": "context", "type": "input"},
                {"id": "analysis", "type": "reasoning"},
                {"id": "risk", "type": "policy"},
                {"id": "decision", "type": "output"},
            ],
            "edges": [
                ["context", "analysis"],
                ["analysis", "risk"],
                ["risk", "decision"],
            ],
            "execution_allowed": False,
        }

    def validate(self):
        graph = self.graph()
        return {"ready": True, "valid": len(graph["nodes"]) >= 1 and len(graph["edges"]) >= 1}

ai_decision_graph_service = AIDecisionGraphService()
