class AIMemorySafetyPolicy:
    def policy(self):
        return {
            "ready": True,
            "yasara_owns_memory": True,
            "provider_owns_memory": False,
            "external_write_allowed": False,
            "sensitive_data_export_allowed": False,
            "tool_execution_allowed": False,
            "execution_allowed": False,
        }

    def can_export(self):
        return {"ready": True, "allowed": False, "reason": "sensitive_data_export_disabled"}

ai_memory_safety_policy = AIMemorySafetyPolicy()
