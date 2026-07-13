from app.platform_core.contracts.base import StandardAPIResponse

def test_v426_standard_response():
    r = StandardAPIResponse(module="x", data={"a": 1}).to_dict()
    assert r["ready"] is True
    assert r["module"] == "x"
    assert r["data"]["a"] == 1
