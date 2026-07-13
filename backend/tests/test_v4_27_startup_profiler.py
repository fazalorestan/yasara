from app.platform_core.extension_host.startup_profiler import StartupProfiler

def test_v427_startup_profiler():
    p = StartupProfiler()
    result = p.measure("x", lambda: "ok")
    assert result["plugin"] == "x"
    assert result["result"] == "ok"
