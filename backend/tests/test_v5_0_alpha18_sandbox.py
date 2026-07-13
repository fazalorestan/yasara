from app.platform_core.exchanges.sdk.sandbox import ExchangeConnectorSandboxContract
def test_v500_alpha18_sandbox():
    p = ExchangeConnectorSandboxContract().policy()
    assert p["kernel_protected"] is True
    assert p["live_orders_allowed"] is False
