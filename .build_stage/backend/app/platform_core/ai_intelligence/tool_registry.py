class AIToolRegistry:
    def __init__(self):
        self._tools = {
            "market.context": {"tool_id": "market.context", "name": "Market Context", "enabled": True, "execution": "disabled"},
            "risk.context": {"tool_id": "risk.context", "name": "Risk Context", "enabled": True, "execution": "disabled"},
        }

    def list_tools(self):
        return {"ready": True, "tools": list(self._tools.values()), "count": len(self._tools)}

    def get(self, tool_id: str):
        tool = self._tools.get(tool_id)
        return {"ready": tool is not None, "tool": tool}

ai_tool_registry = AIToolRegistry()
