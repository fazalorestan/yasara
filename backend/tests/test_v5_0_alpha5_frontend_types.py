from pathlib import Path

def test_v500_alpha5_frontend_types():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "indicators" / "v5-indicator-release-gate-types.ts").exists()
