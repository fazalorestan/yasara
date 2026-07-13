from app.platform_core.enterprise_scheduler.retry import RetryPolicyRegistry

def test_v436_retry_policy():
    r = RetryPolicyRegistry()
    p = r.set_policy("x")
    assert p.max_retries == 3
