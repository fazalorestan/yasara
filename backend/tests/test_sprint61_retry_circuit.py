from app.connectivity_v1.retry_circuit import CircuitBreakerV1, CircuitState, RetryPolicyV1

def test_retry_policy_backoff():
    assert RetryPolicyV1(base_delay_seconds=1).delay_for_attempt(3) == 4

def test_circuit_breaker_opens():
    cb = CircuitBreakerV1(failure_threshold=2)
    cb.record_failure()
    assert cb.allow_request() is True
    assert cb.record_failure() == CircuitState.OPEN
    assert cb.allow_request() is False
