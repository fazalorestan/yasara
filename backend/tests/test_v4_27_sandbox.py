from app.platform_core.extension_host.sandbox import PluginSandbox

def test_v427_sandbox():
    s = PluginSandbox("p")
    started = s.start()
    assert started["state"] == "running"
    stopped = s.stop()
    assert stopped["state"] == "stopped"
