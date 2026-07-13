from pathlib import Path

def test_route_file():
    text = (Path(__file__).resolve().parents[2] / "backend/app/api/v1/routes/v52_enterprise_trading_os_v1.py").read_text(encoding="utf-8")
    assert "/enterprise/trading-os" in text
    assert "/snapshot" in text
