from pathlib import Path

def test_path_1():
 root=Path(__file__).resolve().parents[2]; assert (root/'packaging/windows/YaSara.spec').exists()
