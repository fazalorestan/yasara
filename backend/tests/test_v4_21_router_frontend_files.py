from pathlib import Path

def test_v421_router_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "backend" / "scripts" / "apply_v4_21_market_structure_pro_router_patch.py").exists()
    assert (root / "frontend" / "src" / "api" / "marketStructurePro.ts").exists()
