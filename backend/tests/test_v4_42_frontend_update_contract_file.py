from pathlib import Path

def test_v442_frontend_update_contract_file():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "indicators" / "yasara" / "yasara-update-contract.ts").exists()
