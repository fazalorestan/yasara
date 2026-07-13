from app.platform_core.ai_intelligence.memory_report import ai_memory_context_report

class AIMemoryContextReadinessGate:
    def run(self):
        report = ai_memory_context_report.report()
        ready = report["ready"] and report["safety"]["yasara_owns_memory"] and report["execution_allowed"] is False
        return {
            "ready": ready,
            "checks": {
                "report_ready": report["ready"],
                "yasara_owns_memory": report["safety"]["yasara_owns_memory"],
                "provider_owns_memory": False,
                "external_write_allowed": False,
                "real_provider_connection_allowed": False,
                "execution_allowed": False,
            },
            "execution_allowed": False,
        }

ai_memory_context_readiness_gate = AIMemoryContextReadinessGate()
