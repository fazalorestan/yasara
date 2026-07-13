from pathlib import Path

def test_path_10():
 root=Path(__file__).resolve().parents[2]; assert (root/'scripts/check_yasara_exe_output.py').exists()
