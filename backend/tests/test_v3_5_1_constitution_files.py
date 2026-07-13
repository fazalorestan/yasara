from pathlib import Path

def test_v351_constitution_files_exist():
    root = Path(__file__).resolve().parents[2]
    assert (root / "feature_registry.yaml").exists()
    assert (root / "dependency_graph.yaml").exists()
    assert (root / "docs" / "data_flow.md").exists()
    assert (root / "technical_debt_log.md").exists()
