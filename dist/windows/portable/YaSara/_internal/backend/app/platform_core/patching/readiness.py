from app.platform_core.patching.planner import patch_pipeline_planner
class PatchPipelineReadinessGate:
    def run(self):
        plan = patch_pipeline_planner.build_plan()
        checks = {"planner_ready": plan["ready"], "v5_auto_discovery_enabled": plan["v5_auto_discovery_enabled"], "destructive_actions_allowed": False}
        ready = checks["planner_ready"] and checks["v5_auto_discovery_enabled"]
        return {"ready": ready, "score": 100.0 if ready else 0.0, "plan": plan, "checks": checks}
patch_pipeline_readiness_gate = PatchPipelineReadinessGate()
