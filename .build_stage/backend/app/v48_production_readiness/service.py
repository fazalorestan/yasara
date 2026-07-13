import json
from pathlib import Path
from app.v48_production_readiness.models import BuildProfileRequestV48, ProductionReadinessSummaryV48

ROOT = Path(__file__).resolve().parents[3]


class ProductionReadinessServiceV48:
    def summary(self):
        return ProductionReadinessSummaryV48()

    def manifest(self):
        path = ROOT / "release_manifest.json"
        data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        return {"ready": bool(data), "manifest": data, "live_trading_enabled": False}

    def build_profile_guard(self, request: BuildProfileRequestV48):
        manifest = self.manifest()["manifest"]
        commercial_excludes = manifest.get("commercial_excludes", [])
        if request.build_type == "commercial":
            return {
                "ready": True,
                "build_type": "commercial",
                "execution_engine_allowed": False,
                "trade_api_keys_allowed": False,
                "excluded": commercial_excludes,
                "release_allowed": "execution_engine" in commercial_excludes and "trade_api_keys" in commercial_excludes,
                "live_trading_enabled": False,
            }
        return {
            "ready": True,
            "build_type": "personal",
            "execution_engine_allowed_future": True,
            "requires_license_gate": True,
            "requires_kill_switch": True,
            "requires_risk_guard": True,
            "release_allowed": True,
            "live_trading_enabled": False,
        }

    def environment_health(self):
        required = [
            "feature_registry.yaml",
            "dependency_graph.yaml",
            "feature_flags.yaml",
            "release_manifest.json",
            "technical_debt_log.md",
            "docs/data_flow.md",
            "data/ykb/knowledge_entries.json",
            "backend/app/api/v1/router.py",
            "frontend/src/App.tsx",
        ]
        checks = {item: (ROOT / item).exists() for item in required}
        score = round(sum(1 for v in checks.values() if v) / len(checks) * 100, 2)
        return {"ready": score == 100, "score": score, "checks": checks, "live_trading_enabled": False}

    def security_checklist(self):
        items = {
            "commercial_excludes_execution": self.build_profile_guard(BuildProfileRequestV48(build_type="commercial"))["execution_engine_allowed"] is False,
            "release_manifest_exists": (ROOT / "release_manifest.json").exists(),
            "feature_flags_exists": (ROOT / "feature_flags.yaml").exists(),
            "technical_debt_log_exists": (ROOT / "technical_debt_log.md").exists(),
            "real_execution_disabled": True,
            "api_keys_not_required_for_commercial": True,
        }
        score = round(sum(1 for v in items.values() if v) / len(items) * 100, 2)
        return {"ready": score == 100, "score": score, "items": items, "live_trading_enabled": False}

    def backup_status(self):
        folders = ["data/ykb", "data/backtests", "data/paper_trading", "data/journal", "data/notifications"]
        checks = {folder: (ROOT / folder).exists() for folder in folders}
        return {
            "ready": all(checks.values()),
            "backup_ready_folders": checks,
            "restore_strategy": "file_snapshot_now_database_later",
            "live_trading_enabled": False,
        }

    def final_readiness(self):
        env = self.environment_health()
        sec = self.security_checklist()
        backup = self.backup_status()
        score = round((env["score"] + sec["score"] + (100 if backup["ready"] else 80)) / 3, 2)
        return {
            "ready": score >= 95,
            "final_readiness_percent": score,
            "environment": env,
            "security": sec,
            "backup": backup,
            "recommendation": "ready_for_v4_9_release_candidate" if score >= 95 else "fix_release_blockers",
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }
