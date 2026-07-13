from app.v425_policy_gate.service import PolicyGateServiceV425

def test_v425_service():
    service = PolicyGateServiceV425()
    assert service.summary().ready is True
    assert service.evaluate()["ready"] is True
