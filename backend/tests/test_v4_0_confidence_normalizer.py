from app.v40_market_context.models import EngineResultV40
from app.v40_market_context.normalizer import ConfidenceNormalizerV40

def test_v40_normalizer():
    n = ConfidenceNormalizerV40()
    assert n.normalize(120) == 100
    score = n.weighted_score([EngineResultV40(engine='a', confidence=80, bias='bullish')])
    assert score["bias"] == "bullish"
