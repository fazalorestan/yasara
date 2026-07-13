from app.platform_core.indicators.handoff.migration_checklist import IndicatorMigrationChecklistService

def test_v450_checklist():
    c = IndicatorMigrationChecklistService().checklist()
    assert c["complete"] is True
    assert "final_readiness_gate_passed" in c["items"]
