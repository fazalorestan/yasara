from app.multi_exchange_v1.health import ExchangeHealthEngineV1

def test_exchange_health_report_contains_bitunix_toobit():
    report = ExchangeHealthEngineV1().report()
    exchanges = {item.exchange for item in report.exchanges}
    assert "bitunix" in exchanges
    assert "toobit" in exchanges
    assert report.status == "ok"
