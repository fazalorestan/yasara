from app.platform_core.licensing.readiness.checklist import license_security_checklist
from app.platform_core.licensing.readiness.compatibility import license_compatibility_matrix
from app.platform_core.licensing.readiness.e2e import license_e2e_flow
from app.platform_core.licensing.readiness.handoff import license_subsystem_handoff

class LicenseFinalReadinessGate:
    def run(self):
        e2e = license_e2e_flow.run_demo_flow()
        checklist = license_security_checklist.checklist()
        compatibility = license_compatibility_matrix.matrix()
        handoff = license_subsystem_handoff.handoff()
        ready = e2e["ready"] and checklist["ready"] and compatibility["ready"] and handoff["ready"]
        return {
            "ready": ready,
            "score": 100.0 if ready else 0.0,
            "e2e": e2e,
            "security_checklist": checklist,
            "compatibility": compatibility,
            "handoff": handoff,
            "execution_allowed": False,
            "mode": "license_final_readiness",
        }

license_final_readiness_gate = LicenseFinalReadinessGate()
