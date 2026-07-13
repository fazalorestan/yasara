from app.v414_ai_fusion.fusion import fuse_modules
def test_v414_fusion_core():
    data=fuse_modules([
        {"module":"smart_money","bias":"bullish","confidence":90},
        {"module":"ict","bias":"bullish","confidence":80},
        {"module":"risk","bias":"bullish","confidence":80},
    ])
    assert data["decision"] in ["LONG","SHORT","WAIT"]
    assert data["agreement"]["dominant_bias"] == "bullish"
