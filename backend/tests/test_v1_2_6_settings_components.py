from pathlib import Path
def test_settings_components_exist():
    root = Path(__file__).resolve().parents[2]
    components = root / "frontend" / "src" / "components" / "settings"
    for name in ["SettingsPanel.tsx","ProductionChecklist.tsx","LayoutManager.tsx"]:
        assert (components / name).exists()
