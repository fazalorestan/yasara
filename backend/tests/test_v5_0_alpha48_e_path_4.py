from pathlib import Path

def test_path_4():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/windows_builder/portable_build_contract.py').exists()
