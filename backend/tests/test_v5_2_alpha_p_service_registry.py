from app.platform_core.service_registry.container import ServiceRegistry

def test_service_registry_lazy():
    calls=[]
    r=ServiceRegistry()
    r.register("x", lambda: calls.append(1) or {"ok": True})
    assert calls == []
    assert r.resolve("x")["ok"] is True
    assert r.resolve("x")["ok"] is True
    assert calls == [1]
