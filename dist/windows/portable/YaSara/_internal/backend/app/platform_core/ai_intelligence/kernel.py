class AIKernelService:
    def kernel_status(self):
        return {
            "ready": True,
            "kernel": "yasara_ai_kernel",
            "mode": "contract_only",
            "memory_owned_by_yasara": True,
            "provider_replaceable": True,
            "real_provider_connection": False,
            "execution_allowed": False,
        }

ai_kernel_service = AIKernelService()
