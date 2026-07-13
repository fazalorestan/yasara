from app.platform_core.extension_host.host import ExtensionHost

def test_v427_extension_host_load():
    h = ExtensionHost()
    r = h.load_catalog()
    assert r["ready"] is True
    assert r["plugin_count"] >= 5
