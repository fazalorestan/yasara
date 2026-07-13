from app.connectivity_v1.synchronizer import OrderPositionSynchronizerV1, SyncItemV1

def test_order_position_synchronizer_compare():
    local = [SyncItemV1(item_id="o1", status="ok")]
    remote = [SyncItemV1(item_id="o1", status="ok"), SyncItemV1(item_id="o2", status="ok")]
    result = OrderPositionSynchronizerV1().compare(local, remote)
    assert result.synced == 1
    assert result.missing == 1
