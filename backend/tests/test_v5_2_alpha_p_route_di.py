from pathlib import Path

def test_portfolio_route_di():
    text=(Path(__file__).resolve().parents[2]/"backend/app/api/v1/routes/portfolio_v1.py").read_text(encoding="utf-8")
    assert "Depends(get_portfolio_intelligence_service_v1)" in text
