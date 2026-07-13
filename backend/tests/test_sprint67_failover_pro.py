from app.connectivity_v1.failover_pro import FailoverCandidateV1, FailoverProEngineV1

def test_failover_pro_selects_lowest_latency():
    result = FailoverProEngineV1().choose([
        FailoverCandidateV1(name="a", healthy=True, latency_ms=100),
        FailoverCandidateV1(name="b", healthy=True, latency_ms=50),
    ])
    assert result.selected == "b"
