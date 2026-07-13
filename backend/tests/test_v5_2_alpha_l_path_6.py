from pathlib import Path

def test_path_6():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/force_merge_k_sqlalchemy_gate/report.py').exists()
