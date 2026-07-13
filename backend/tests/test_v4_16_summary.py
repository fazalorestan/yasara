from app.v416_neowave_sprint2.service import NeoWaveSprint2ServiceV416
def test_v416_summary():
    s=NeoWaveSprint2ServiceV416().summary()
    assert s.ready is True
    assert s.constitution_compliant is True
