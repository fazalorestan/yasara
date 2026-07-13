from app.platform_core.extension_host.resource_quota import ResourceQuotaReporter

def test_v427_resource_quota():
    r = ResourceQuotaReporter()
    q = r.set_quota("p")
    assert q["enforced"] is False
    assert q["mode"] == "report_only"
