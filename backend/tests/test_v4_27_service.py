from app.v427_extension_host.service import ExtensionHostServiceV427

def test_v427_service():
    s = ExtensionHostServiceV427()
    assert s.summary().ready is True
    assert s.load_catalog()["ready"] is True
    assert s.health()["ready"] is True
