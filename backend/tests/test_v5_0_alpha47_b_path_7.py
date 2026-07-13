from pathlib import Path

def test_path_7():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/ci_pipeline/test_report.py').exists()
