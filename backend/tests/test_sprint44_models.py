from app.v52_ai_decision_engine.models import FusionRequest
def test_request(): assert FusionRequest(symbol="BTCUSDT", timeframe="4h").symbol == "BTCUSDT"
