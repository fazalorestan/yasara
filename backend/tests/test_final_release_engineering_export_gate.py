from app.final_release_engineering_v1.release_export_gate import ReleaseExportGateBuilderV1

def test_release_export_gate():
    gate = ReleaseExportGateBuilderV1().build()
    assert gate.passed is True
