from app.connectivity_v1.load_balancer import ExchangeLoadBalancerV1, ExchangeLoadCandidateV1

def test_exchange_load_balancer_prefers_lower_load():
    selected = ExchangeLoadBalancerV1().choose([
        ExchangeLoadCandidateV1(name="a", current_load=0.8, latency_ms=10),
        ExchangeLoadCandidateV1(name="b", current_load=0.1, latency_ms=50),
    ])
    assert selected.name == "b"
