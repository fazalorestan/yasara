from pathlib import Path

def test_path_12():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_2_ALPHA_APSCHEDULER_DEPENDENCY_GATE_PATCH.md').exists()
