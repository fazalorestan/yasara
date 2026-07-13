from app.platform_core.api_health.report import api_health_report_builder

class APISmokeReadinessGate:
    def run(self):
        report = api_health_report_builder.build()
        return {"ready": report["ready"], "score": 100.0 if report["ready"] else 0.0, "report": report, "execution_allowed": False, "mode": "api_smoke_health"}

api_smoke_readiness_gate = APISmokeReadinessGate()
