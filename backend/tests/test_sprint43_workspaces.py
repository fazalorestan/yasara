from pathlib import Path

def test_all_workspaces_present():
    text = (Path(__file__).resolve().parents[2] / "frontend/src/components/enterprise/EnterpriseTradingOS.tsx").read_text(encoding="utf-8")
    for token in ["Trader", "AI Analyst", "Portfolio", "Developer"]:
        assert token in text
