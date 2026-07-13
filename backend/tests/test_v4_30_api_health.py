from app.platform_core.diagnostics.api_health import APIHealthAggregator

def test_v430_api_health():
    result = APIHealthAggregator().run()
    assert result.ready is True
    assert result.data["endpoint_count"] >= 5
