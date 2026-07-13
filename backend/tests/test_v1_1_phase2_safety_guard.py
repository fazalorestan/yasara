from app.v11_exchange_connectivity.safety import ExchangeSafetyGuardV11

def test_safety_guard_blocks_signed_and_post():
    guard = ExchangeSafetyGuardV11()
    assert guard.assert_request_allowed(signed=False, method="GET") is True
    assert guard.assert_request_allowed(signed=True, method="GET") is False
    assert guard.assert_request_allowed(signed=False, method="POST") is False
