from app.final_delivery_pack_v1.delivery_pack_summary import DeliveryPackSummaryBuilderV1

def test_delivery_pack_summary():
    summary = DeliveryPackSummaryBuilderV1().build()
    assert summary.ready is True
    assert summary.version == "1.0.0"
