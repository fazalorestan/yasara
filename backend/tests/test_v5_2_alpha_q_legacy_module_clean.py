from pathlib import Path

def test_legacy_module_no_literal_newlines():
    root = Path(__file__).resolve().parents[2]
    files = [
        "backend/app/platform_core/legacy_marker_launcher_sync_diagnostics/report.py",
        "backend/app/platform_core/legacy_marker_launcher_sync_diagnostics/readiness.py",
        "backend/app/v52_alpha_legacy_marker_launcher_sync_diagnostics/models.py",
        "backend/app/v52_alpha_legacy_marker_launcher_sync_diagnostics/service.py",
        "backend/app/api/v1/routes/v52_alpha_legacy_marker_launcher_sync_diagnostics_v1.py",
    ]
    for rel in files:
        text = (root / rel).read_text(encoding="utf-8")
        assert "\\n" not in text
