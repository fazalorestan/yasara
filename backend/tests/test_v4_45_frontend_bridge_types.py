from pathlib import Path

def test_v445_frontend_bridge_types():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "indicators" / "yasara" / "yasara-engine-bridge-types.ts").exists()
