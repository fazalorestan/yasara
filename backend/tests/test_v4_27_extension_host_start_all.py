from app.platform_core.extension_host.host import ExtensionHost

def test_v427_extension_host_start_all():
    h = ExtensionHost()
    r = h.start_all()
    assert r["ready"] is True
    assert r["started_count"] >= 5
