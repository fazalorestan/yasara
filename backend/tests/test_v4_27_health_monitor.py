from app.platform_core.extension_host.health_monitor import PluginHealthMonitor

def test_v427_health_monitor():
    h = PluginHealthMonitor()
    h.set("p", "healthy")
    assert h.get("p")["state"] == "healthy"
