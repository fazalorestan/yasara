from app.v11_paper_trading.models import PaperPositionV11
from app.v11_risk_control.position_risk import PositionRiskCheckerV11

def test_position_risk_blocks_large_position():
    position = PaperPositionV11(exchange="binance", symbol="BTCUSDT", quantity=1, avg_price=50000)
    result = PositionRiskCheckerV11().check_positions([position])
    assert result.allowed is False
