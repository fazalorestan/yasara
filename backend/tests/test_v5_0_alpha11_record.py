from app.platform_core.licensing.activation.record import OfflineActivationRecord
def test_v500_alpha11_record():
    r = OfflineActivationRecord("KEY", "FP").to_dict()
    assert r["license_key"] == "KEY"
    assert r["status"] == "active"
