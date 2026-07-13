class AIAgentRegistry:
    def __init__(self):
        self._agents = {
            "analyst.agent": {"agent_id": "analyst.agent", "role": "analysis", "enabled": True, "execution": "disabled"},
            "risk.agent": {"agent_id": "risk.agent", "role": "risk", "enabled": True, "execution": "disabled"},
        }

    def list_agents(self):
        return {"ready": True, "agents": list(self._agents.values()), "count": len(self._agents)}

    def get(self, agent_id: str):
        agent = self._agents.get(agent_id)
        return {"ready": agent is not None, "agent": agent}

ai_agent_registry = AIAgentRegistry()
