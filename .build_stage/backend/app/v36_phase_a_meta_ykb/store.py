import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
YKB_DIR = ROOT / "data" / "ykb"
YKB_ENTRIES = YKB_DIR / "knowledge_entries.json"
YKB_MEMORY = YKB_DIR / "engine_memory.json"
FEATURE_REGISTRY = ROOT / "feature_registry.yaml"
DEPENDENCY_GRAPH = ROOT / "dependency_graph.yaml"
TECH_DEBT = ROOT / "technical_debt_log.md"
DATA_FLOW = ROOT / "docs" / "data_flow.md"


class PhaseAMetaStoreV36:
    def __init__(self):
        YKB_DIR.mkdir(parents=True, exist_ok=True)
        if not YKB_ENTRIES.exists():
            YKB_ENTRIES.write_text(json.dumps({"entries": []}, indent=2), encoding="utf-8")
        if not YKB_MEMORY.exists():
            YKB_MEMORY.write_text(json.dumps({"memories": []}, indent=2), encoding="utf-8")

    def read_json(self, path, default):
        if not path.exists():
            path.write_text(json.dumps(default, indent=2, ensure_ascii=False), encoding="utf-8")
        return json.loads(path.read_text(encoding="utf-8"))

    def write_json(self, path, data):
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        return data

    def now(self):
        return datetime.now(timezone.utc).isoformat()

    def list_ykb_entries(self):
        return self.read_json(YKB_ENTRIES, {"entries": []})["entries"]

    def add_ykb_entry(self, entry):
        data = self.read_json(YKB_ENTRIES, {"entries": []})
        item = entry.model_dump()
        if item.get("created_at") == "auto":
            item["created_at"] = self.now()
        data["entries"].append(item)
        self.write_json(YKB_ENTRIES, data)
        return item

    def get_feature_registry_text(self):
        return FEATURE_REGISTRY.read_text(encoding="utf-8") if FEATURE_REGISTRY.exists() else ""

    def get_dependency_graph_text(self):
        return DEPENDENCY_GRAPH.read_text(encoding="utf-8") if DEPENDENCY_GRAPH.exists() else ""

    def get_data_flow_text(self):
        return DATA_FLOW.read_text(encoding="utf-8") if DATA_FLOW.exists() else ""

    def get_tech_debt_text(self):
        return TECH_DEBT.read_text(encoding="utf-8") if TECH_DEBT.exists() else ""

    def append_technical_debt(self, item):
        line = f"| {item.id} | {item.type} | {item.description} | {item.status} | {item.priority} |\n"
        if not TECH_DEBT.exists():
            TECH_DEBT.write_text("# Technical Debt Log\n\n| ID | Type | Description | Status | Priority |\n|---|---|---|---|---|\n", encoding="utf-8")
        with TECH_DEBT.open("a", encoding="utf-8") as f:
            f.write(line)
        return item.model_dump()
