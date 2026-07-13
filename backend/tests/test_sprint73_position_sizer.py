from app.ai_trading_v1.position_sizer import PositionSizerAIV1, PositionSizingInputV1

def test_position_sizer_ai():
    result = PositionSizerAIV1().calculate(PositionSizingInputV1(equity=10000, risk_percent=1, stop_loss_percent=2, confidence=80))
    assert result.risk_amount == 100
    assert result.position_size == 5000
