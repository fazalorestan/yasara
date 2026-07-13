from pathlib import Path

def test_path_20():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha44_pic_core/service.py').exists()
