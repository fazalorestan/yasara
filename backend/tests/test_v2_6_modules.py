from app.v26_final_operational.service import FinalOperationalBridgeServiceV26

def test_v26_modules():
    data = FinalOperationalBridgeServiceV26().modules()
    assert data["ready"] is True
    assert len(data["modules"]) >= 5
    assert all(item["ready"] for item in data["modules"])
