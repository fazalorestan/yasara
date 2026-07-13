from pathlib import Path

def test_path_8():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/stabilization/technical_debt_report.py').exists()
