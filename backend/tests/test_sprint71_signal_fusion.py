from app.ai_trading_v1.signal_fusion import SignalFusionEngineV1, SignalInputV1

def test_signal_fusion_long():
    result = SignalFusionEngineV1().fuse([
        SignalInputV1(source="rsi", direction="long", confidence=80),
        SignalInputV1(source="trend", direction="long", confidence=70),
    ])
    assert result.direction == "long"
    assert result.sources == 2
