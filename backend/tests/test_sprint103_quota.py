from app.cloud_v1.quota import QuotaServiceV1, QuotaStateV1

def test_quota_remaining():
    service = QuotaServiceV1()
    quota = QuotaStateV1(used=5, limit=10)
    assert service.remaining(quota) == 5
    assert service.allowed(quota, 6) is False
