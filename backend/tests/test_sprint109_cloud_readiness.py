from app.cloud_v1.readiness import CloudReadinessBuilderV1

def test_cloud_readiness():
    report = CloudReadinessBuilderV1().build()
    assert report.ready is True
    assert "auth" in report.modules
