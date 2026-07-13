from pathlib import Path
def test_react_component_files_exist():
    root = Path(__file__).resolve().parents[2]
    components = root / "frontend" / "src" / "components"
    assert (components / "Sidebar.tsx").exists()
    assert (components / "Header.tsx").exists()
    assert (components / "MetricCard.tsx").exists()
    assert (components / "Panel.tsx").exists()
