from app.final_package_v1.final_export_gate import FinalExportGateBuilderV1

def test_final_export_gate():
    gate = FinalExportGateBuilderV1().build()
    assert gate.passed is True
