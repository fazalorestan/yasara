from pathlib import Path

def test_v351_scripts_exist():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v3_5_1_constitution_audit_router_patch.py").exists()
    assert (root / "scripts" / "yasara_v4_project_audit.py").exists()
    assert (root / "scripts" / "sync_operational_frontend_status.py").exists()
