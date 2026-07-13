from pathlib import Path

def test_v36_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "data" / "ykb" / "knowledge_entries.json").exists()
    assert (root / "feature_registry.yaml").exists()
    assert (root / "dependency_graph.yaml").exists()
    assert (root / "docs" / "data_flow.md").exists()
