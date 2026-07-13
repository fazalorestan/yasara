from app.v414_ai_fusion.fusion import explain, fuse_modules
def test_v414_explain():
    f=fuse_modules([{"module":"indicator","bias":"neutral","confidence":50}])
    e=explain(f)
    assert isinstance(e, list)
    assert len(e) > 0
