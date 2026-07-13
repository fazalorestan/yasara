from pathlib import Path

def test_portfolio_lazy_service():
    text=(Path(__file__).resolve().parents[2]/"backend/app/portfolio_v1/application/service.py").read_text(encoding="utf-8")
    assert "portfolio_intelligence_service_v1 =" not in text
    assert "get_portfolio_intelligence_service_v1" in text
    assert "service_registry.register" in text
