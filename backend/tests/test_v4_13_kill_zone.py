from app.v413_ict_engine.detectors import kill_zone
def test_v413_kill_zone():
    assert kill_zone(8*3600)["zone"] == "london"
    assert kill_zone(13*3600)["zone"] == "new_york"
