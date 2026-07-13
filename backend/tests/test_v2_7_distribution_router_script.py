from pathlib import Path

def test_v27_distribution_router_script():
    root = Path(__file__).resolve().parents[1]
    script = root / "scripts" / "apply_v2_7_distribution_router_patch.py"
    assert script.exists()
    assert "v27_distribution_v1" in script.read_text(encoding="utf-8")
