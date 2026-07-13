class AISessionMemoryService:
    def session(self, session_id: str = "ai-session-001"):
        return {
            "ready": True,
            "session_id": session_id,
            "items": [{"role": "user", "content": "simulated request"}],
            "memory_scope": "session",
            "provider_owned": False,
        }

ai_session_memory_service = AISessionMemoryService()
