from app.production_freeze_v1.production_freeze_gate import ProductionFreezeGateBuilderV1

def test_production_freeze_gate():
    gate = ProductionFreezeGateBuilderV1().build()
    assert gate.passed is True
