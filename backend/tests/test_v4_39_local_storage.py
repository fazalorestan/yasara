from app.platform_core.enterprise_storage.local import LocalStorageEngine

def test_v439_local_storage():
    s = LocalStorageEngine()
    s.write("b", "k", {"x": 1})
    assert s.read("b", "k").payload["x"] == 1
    assert len(s.list("b")) == 1
