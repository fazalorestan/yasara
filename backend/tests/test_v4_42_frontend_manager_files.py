from pathlib import Path

def test_v442_frontend_manager_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "indicators" / "chart-indicator-manager.ts").exists()
    assert (root / "frontend" / "src" / "indicators" / "yasara" / "yasara-renderer-contract.ts").exists()
