from app.platform_core.licensing.activation.record import OfflineActivationRecord
from app.platform_core.licensing.activation.store import ActivationRecordStore
def test_v500_alpha11_store_add_count():
    s = ActivationRecordStore()
    s.add(OfflineActivationRecord("KEY", "FP"))
    assert s.count_for_license("KEY") == 1
