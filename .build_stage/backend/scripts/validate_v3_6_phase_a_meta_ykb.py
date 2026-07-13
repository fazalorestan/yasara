from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
required = [
    ROOT / "feature_registry.yaml",
    ROOT / "dependency_graph.yaml",
    ROOT / "docs" / "data_flow.md",
    ROOT / "technical_debt_log.md",
    ROOT / "data" / "ykb" / "knowledge_entries.json",
]

missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
if missing:
    print("Missing Phase A files:")
    for item in missing:
        print("-", item)
    sys.exit(1)

dep = (ROOT / "dependency_graph.yaml").read_text(encoding="utf-8")
if "execution_engine" not in dep or "excludes" not in dep:
    print("Missing commercial execution exclusion in dependency graph.")
    sys.exit(1)

print("YaSara v3.6 Phase A validation PASSED.")
