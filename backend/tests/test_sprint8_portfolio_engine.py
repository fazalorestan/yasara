from app.decision_v1.domain.models import DecisionDirection
from app.portfolio_v1.domain.models import PortfolioPosition, PortfolioSnapshot
from app.portfolio_v1.engine.portfolio_engine import PortfolioIntelligenceEngineV1

def test_portfolio_engine_report():
    snapshot = PortfolioSnapshot(equity=10000, cash=5000, positions=[
        PortfolioPosition(symbol='BTC/USDT', direction=DecisionDirection.LONG, quantity=0.05, entry_price=60000, mark_price=62000),
        PortfolioPosition(symbol='ETH/USDT', direction=DecisionDirection.LONG, quantity=1.0, entry_price=3000, mark_price=3100),
    ])
    report = PortfolioIntelligenceEngineV1().analyze(snapshot)
    assert report.exposure.total_exposure > 0
    assert report.allocation.items
    assert report.risk.final_risk_score >= 0
