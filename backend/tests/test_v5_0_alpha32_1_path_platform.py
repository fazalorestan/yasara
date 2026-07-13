from pathlib import Path

def test_v500_alpha32_1_path_platform():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/patch_runner_definitive/service.py').exists()
