from app.platform_core.indicators.pine_source.update_contract import PineUpdateSafetyContractService

def test_v444_update_contract():
    c = PineUpdateSafetyContractService().contract()
    assert c["destructive"] is False
    assert c["editable_file"].endswith("yasara-v1.pine")
