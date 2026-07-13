from app.v52_ai_decision_engine.models import FusionRequest
from app.v52_ai_decision_engine.services.fusion_service import FusionService
def test_wait(): assert FusionService().fuse(FusionRequest(symbol="BTCUSDT", timeframe="4h")).decision.value == "WAIT"
