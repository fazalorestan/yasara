from pathlib import Path
def test_workspace_settings_data_exists():
    root = Path(__file__).resolve().parents[2]
    text = (root / "frontend" / "src" / "data" / "workspaceSettings.ts").read_text(encoding="utf-8")
    assert "workspacePresets" in text
    assert "themeOptions" in text
    assert "productionChecklist" in text
