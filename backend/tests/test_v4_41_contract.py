from app.platform_core.indicators.yasara_contract import YaSaraIndicatorContract

def test_v441_contract():
    c = YaSaraIndicatorContract().overlay_contract()
    assert c["indicator"] == "yasara"
    assert "EMA21" in c["overlays"]
    assert "BOS" in c["signals"]
