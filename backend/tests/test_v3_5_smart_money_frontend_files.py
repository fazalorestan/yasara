from pathlib import Path

def test_v35_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "smartMoney.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "SmartMoneyStatus.tsx").exists()
