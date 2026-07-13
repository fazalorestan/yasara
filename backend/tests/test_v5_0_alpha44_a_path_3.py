from pathlib import Path

def test_path_3():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/api/v1/routes/v500_alpha44_pic_core_v1.py').exists()
