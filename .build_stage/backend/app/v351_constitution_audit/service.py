from pathlib import Path


class ConstitutionAuditServiceV351:
    def __init__(self):
        self.root = Path(__file__).resolve().parents[3]

    def summary(self):
        return {
            "ready": True,
            "phase": "v3_5_1_constitution_audit_repair",
            "constitution_version": "YASARA_MASTER_REQUIREMENTS_FINAL_V4",
            "product_progress_percent": 78,
            "next_recommended_phase": "phase_a_meta_infrastructure_completion",
            "safety": "audit_only_live_trading_disabled",
        }

    def health(self):
        checks = {
            "feature_registry": (self.root / "feature_registry.yaml").exists(),
            "dependency_graph": (self.root / "dependency_graph.yaml").exists(),
            "data_flow_doc": (self.root / "docs" / "data_flow.md").exists(),
            "technical_debt_log": (self.root / "technical_debt_log.md").exists(),
            "frontend_app": (self.root / "frontend" / "src" / "App.tsx").exists(),
            "backend_router": (self.root / "backend" / "app" / "api" / "v1" / "router.py").exists(),
        }
        return {
            "ready": all(checks.values()),
            "checks": checks,
            "overall_health_percent": round(sum(1 for v in checks.values() if v) / len(checks) * 100, 2),
            "live_trading_enabled": False,
        }

    def recommendations(self):
        return {
            "ready": True,
            "items": [
                "Complete Phase A meta-infrastructure before adding more large engines.",
                "Auto-sync frontend operational status components into App.tsx after each patch.",
                "Move JSON stores to production database in the next infrastructure milestone.",
                "Create commercial build profile that excludes execution_engine completely.",
                "Start YKB early to avoid future migration of strategy/backtest/AI memory data.",
                "Add CI check for dependency_graph.yaml and feature_registry.yaml.",
            ],
            "live_trading_enabled": False,
        }
