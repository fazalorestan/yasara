from pathlib import Path

def test_frontend_real_data_only():
    root = Path(__file__).resolve().parents[2]
    api = (root / "frontend/src/api/enterpriseTradingOS.ts").read_text(encoding="utf-8")
    ui = (root / "frontend/src/components/enterprise/EnterpriseTradingOS.tsx").read_text(encoding="utf-8")
    assert 'fetch("/api/v1/enterprise/trading-os/snapshot"' in api
    assert "mock" not in ui.lower()
