from app.production_freeze_v1.production_freeze_summary import ProductionFreezeSummaryBuilderV1

def test_production_freeze_summary():
    summary = ProductionFreezeSummaryBuilderV1().build()
    assert summary.ready is True
    assert summary.version == "1.0.0"
