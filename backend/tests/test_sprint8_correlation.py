import math
from app.portfolio_v1.engine.correlation import CorrelationEngineV1
from app.portfolio_v1.domain.models import PortfolioPosition, PortfolioSnapshot
from app.decision_v1.domain.models import DecisionDirection

def test_correlation_matrix():
    snapshot = PortfolioSnapshot(
        equity=10000,
        positions=[
            PortfolioPosition(symbol="BTC/USDT", direction=DecisionDirection.LONG, quantity=1, entry_price=1, mark_price=1),
            PortfolioPosition(symbol="ETH/USDT", direction=DecisionDirection.LONG, quantity=1, entry_price=1, mark_price=1),
        ],
    )
    matrix = CorrelationEngineV1().calculate(
        snapshot,
        {
            "BTC/USDT": [1, 2, 3, 4],
            "ETH/USDT": [1, 2, 3, 4],
        },
    )
    assert math.isclose(matrix.pairs[0].correlation, 1.0, rel_tol=1e-9, abs_tol=1e-9)
    assert matrix.high_correlation_count == 1
