from pathlib import Path
def test_v411_router_script():
    root=Path(__file__).resolve().parents[1]
    assert (root/"scripts"/"apply_v4_11_smart_money_pro_router_patch.py").exists()
