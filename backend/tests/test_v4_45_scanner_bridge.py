from app.platform_core.indicators.bridges.scanner_bridge import IndicatorScannerBridge

def test_v445_scanner_bridge():
    out = IndicatorScannerBridge().to_scanner_item("BTCUSDT", {"signals": [{"direction": "SHORT", "confidence": 55}]})
    assert out["symbol"] == "BTCUSDT"
    assert out["indicator"] == "yasara"
