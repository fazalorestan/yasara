from pathlib import Path

def test_path_4():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/release_candidate/safety_toggle_policy.py').exists()
