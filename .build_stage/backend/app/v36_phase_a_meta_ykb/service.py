from pathlib import Path
from app.v36_phase_a_meta_ykb.models import PhaseAMetaSummaryV36, TechnicalDebtItemV36, YKBEntryV36
from app.v36_phase_a_meta_ykb.store import PhaseAMetaStoreV36, ROOT, FEATURE_REGISTRY, DEPENDENCY_GRAPH, DATA_FLOW, TECH_DEBT, YKB_ENTRIES


class PhaseAMetaYKBServiceV36:
    def __init__(self):
        self.store = PhaseAMetaStoreV36()

    def summary(self):
        return PhaseAMetaSummaryV36()

    def ykb_status(self):
        entries = self.store.list_ykb_entries()
        return {
            "ready": True,
            "entries_count": len(entries),
            "ykb_path": str(YKB_ENTRIES.relative_to(ROOT)),
            "categories": ["strategies", "backtests", "smart_money_rules", "exchange_behavior", "engine_performance", "ai_memory"],
            "live_trading_enabled": False,
        }

    def list_ykb(self):
        return {"ready": True, "items": self.store.list_ykb_entries(), "live_trading_enabled": False}

    def add_ykb(self, entry: YKBEntryV36):
        return {"ready": True, "entry": self.store.add_ykb_entry(entry), "live_trading_enabled": False}

    def registry_status(self):
        text = self.store.get_feature_registry_text()
        features_count = text.count("- key:")
        return {
            "ready": FEATURE_REGISTRY.exists(),
            "path": str(FEATURE_REGISTRY.relative_to(ROOT)),
            "features_count": features_count,
            "has_execution_engine_guard": "commercial_included: false" in text or "commercial_distribution" in text,
            "live_trading_enabled": False,
        }

    def dependency_status(self):
        text = self.store.get_dependency_graph_text()
        return {
            "ready": DEPENDENCY_GRAPH.exists(),
            "path": str(DEPENDENCY_GRAPH.relative_to(ROOT)),
            "has_commercial_execution_exclusion": "execution_engine" in text and "excludes" in text,
            "has_ai_dependencies": "ai_engine_full" in text,
            "live_trading_enabled": False,
        }

    def data_flow_status(self):
        text = self.store.get_data_flow_text()
        return {
            "ready": DATA_FLOW.exists(),
            "path": str(DATA_FLOW.relative_to(ROOT)),
            "has_personal_path": "Personal-only path" in text,
            "has_commercial_path": "Commercial path" in text,
            "live_trading_enabled": False,
        }

    def technical_debt_status(self):
        text = self.store.get_tech_debt_text()
        open_count = text.count("| TD-")
        return {
            "ready": TECH_DEBT.exists(),
            "path": str(TECH_DEBT.relative_to(ROOT)),
            "items_count": open_count,
            "live_trading_enabled": False,
        }

    def add_technical_debt(self, item: TechnicalDebtItemV36):
        return {"ready": True, "item": self.store.append_technical_debt(item), "live_trading_enabled": False}

    def health_score(self):
        checks = {
            "feature_registry": self.registry_status()["ready"],
            "dependency_graph": self.dependency_status()["ready"],
            "data_flow_doc": self.data_flow_status()["ready"],
            "technical_debt_log": self.technical_debt_status()["ready"],
            "ykb_foundation": YKB_ENTRIES.exists(),
            "commercial_execution_exclusion": self.dependency_status()["has_commercial_execution_exclusion"],
        }
        score = round(sum(1 for ok in checks.values() if ok) / len(checks) * 100, 2)
        return {
            "ready": score >= 80,
            "overall_health_percent": score,
            "checks": checks,
            "phase_a_ready": score == 100,
            "live_trading_enabled": False,
        }

    def recommendations(self):
        return {
            "ready": True,
            "items": [
                "Next: add CI validation for feature_registry.yaml and dependency_graph.yaml.",
                "Next: persist YKB to database when DB migration phase starts.",
                "Next: connect AI Engine and Backtest results to YKB entries.",
                "Next: add Error Recovery Engine scenarios in Phase B.",
                "Next: ensure Commercial build excludes execution_engine at packaging level.",
            ],
            "live_trading_enabled": False,
        }
