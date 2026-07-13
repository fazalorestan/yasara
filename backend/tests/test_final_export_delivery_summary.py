from app.final_export_v1.final_delivery_summary import FinalDeliverySummaryBuilderV1

def test_final_delivery_summary():
    summary = FinalDeliverySummaryBuilderV1().build()
    assert summary.ready is True
    assert summary.release_name == "YaSara Professional v1.0 Stable"
