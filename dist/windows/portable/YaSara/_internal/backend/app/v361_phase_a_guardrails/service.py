import json
from pathlib import Path
from app.v361_phase_a_guardrails.models import FeatureValidationRequestV361, PhaseAGuardrailsSummaryV361, YKBSearchRequestV361

ROOT = Path(__file__).resolve().parents[3]
FEATURE_REGISTRY = ROOT / "feature_registry.yaml"
DEPENDENCY_GRAPH = ROOT / "dependency_graph.yaml"
FEATURE_FLAGS = ROOT / "feature_flags.yaml"
YKB_ENTRIES = ROOT / "data" / "ykb" / "knowledge_entries.json"
TECH_DEBT = ROOT / "technical_debt_log.md"


class PhaseAGuardrailsServiceV361:
    def summary(self):
        return PhaseAGuardrailsSummaryV361()

    def _read_text(self, path: Path) -> str:
        return path.read_text(encoding="utf-8") if path.exists() else ""

    def _read_ykb(self):
        if not YKB_ENTRIES.exists():
            return {"entries": []}
        return json.loads(YKB_ENTRIES.read_text(encoding="utf-8"))

    def registry_validation(self):
        text = self._read_text(FEATURE_REGISTRY)
        required_tokens = [
            "market_analysis_engine",
            "smart_money_engine",
            "strategy_builder_core",
            "execution_engine",
            "commercial_included: false",
        ]
        results = {token: token in text for token in required_tokens}
        return {
            "ready": all(results.values()) and FEATURE_REGISTRY.exists(),
            "path": str(FEATURE_REGISTRY.relative_to(ROOT)),
            "checks": results,
            "features_count": text.count("- key:"),
            "live_trading_enabled": False,
        }

    def dependency_validation(self):
        text = self._read_text(DEPENDENCY_GRAPH)
        required_tokens = [
            "market_analysis_engine:",
            "smart_money_engine:",
            "ai_engine_full:",
            "execution_engine:",
            "commercial_distribution:",
            "excludes:",
        ]
        results = {token: token in text for token in required_tokens}
        return {
            "ready": all(results.values()) and DEPENDENCY_GRAPH.exists(),
            "path": str(DEPENDENCY_GRAPH.relative_to(ROOT)),
            "checks": results,
            "live_trading_enabled": False,
        }

    def feature_flags_status(self):
        text = self._read_text(FEATURE_FLAGS)
        return {
            "ready": FEATURE_FLAGS.exists(),
            "path": str(FEATURE_FLAGS.relative_to(ROOT)),
            "execution_engine_disabled": "execution_engine:" in text and "enabled: false" in text,
            "commercial_execution_excluded": "commercial_included: false" in text,
            "flags_count": text.count("enabled:"),
            "live_trading_enabled": False,
        }

    def validate_new_feature(self, request: FeatureValidationRequestV361):
        registry = self._read_text(FEATURE_REGISTRY)
        dependency = self._read_text(DEPENDENCY_GRAPH)
        flags = self._read_text(FEATURE_FLAGS)

        already_exists = request.feature_key in registry
        missing_dependencies = [dep for dep in request.dependencies if dep not in registry and dep not in dependency]
        scope_ok = request.scope in ["shared", "personal_only", "commercial_only"]

        commercial_guard_ok = True
        if request.feature_key == "execution_engine" or request.scope == "personal_only":
            commercial_guard_ok = "commercial_included: false" in registry or "commercial_included: false" in flags

        return {
            "ready": scope_ok and not missing_dependencies and commercial_guard_ok,
            "feature_key": request.feature_key,
            "already_exists": already_exists,
            "missing_dependencies": missing_dependencies,
            "scope_ok": scope_ok,
            "commercial_guard_ok": commercial_guard_ok,
            "decision": "approved" if scope_ok and not missing_dependencies and commercial_guard_ok else "blocked",
            "live_trading_enabled": False,
        }

    def ykb_search(self, request: YKBSearchRequestV361):
        data = self._read_ykb()
        query = request.query.lower().strip()
        tags = {tag.lower() for tag in request.tags}
        results = []
        for entry in data.get("entries", []):
            entry_text = " ".join([
                str(entry.get("id", "")),
                str(entry.get("title", "")),
                str(entry.get("type", "")),
                str(entry.get("content", "")),
                " ".join(entry.get("tags", [])),
            ]).lower()
            tag_match = not tags or bool(tags.intersection({t.lower() for t in entry.get("tags", [])}))
            type_match = request.entry_type is None or entry.get("type") == request.entry_type
            query_match = not query or query in entry_text
            if tag_match and type_match and query_match:
                results.append(entry)
        return {
            "ready": True,
            "query": request.query,
            "count": len(results[:request.limit]),
            "items": results[:request.limit],
            "live_trading_enabled": False,
        }

    def ykb_stats(self):
        data = self._read_ykb()
        entries = data.get("entries", [])
        by_type = {}
        by_scope = {}
        for item in entries:
            by_type[item.get("type", "unknown")] = by_type.get(item.get("type", "unknown"), 0) + 1
            by_scope[item.get("scope", "unknown")] = by_scope.get(item.get("scope", "unknown"), 0) + 1
        return {
            "ready": True,
            "entries_count": len(entries),
            "by_type": by_type,
            "by_scope": by_scope,
            "live_trading_enabled": False,
        }

    def health_aggregate(self):
        registry = self.registry_validation()
        dependency = self.dependency_validation()
        flags = self.feature_flags_status()
        ykb = self.ykb_stats()
        checks = {
            "registry": registry["ready"],
            "dependency_graph": dependency["ready"],
            "feature_flags": flags["ready"],
            "ykb": ykb["ready"],
            "execution_engine_safe": flags["execution_engine_disabled"],
            "commercial_guard": flags["commercial_execution_excluded"],
        }
        score = round(sum(1 for v in checks.values() if v) / len(checks) * 100, 2)
        return {
            "ready": score >= 85,
            "overall_health_percent": score,
            "checks": checks,
            "phase_a_guardrails_ready": score == 100,
            "live_trading_enabled": False,
        }

    def recommendations(self):
        return {
            "ready": True,
            "items": [
                "Before any new feature, call /feature/validate and register it.",
                "Connect future AI, Backtest, Risk and Journal events to YKB.",
                "Move feature_registry.yaml and dependency_graph.yaml validation into CI.",
                "Keep execution_engine disabled until Personal-only build isolation exists.",
                "Next feature phase should start Phase B only after guardrails are green.",
            ],
            "live_trading_enabled": False,
        }
