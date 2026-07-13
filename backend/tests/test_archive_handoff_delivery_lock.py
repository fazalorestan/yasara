from app.archive_handoff_v1.stable_delivery_lock import StableDeliveryLockBuilderV1

def test_stable_delivery_lock():
    lock = StableDeliveryLockBuilderV1().build()
    assert lock.ready is True
