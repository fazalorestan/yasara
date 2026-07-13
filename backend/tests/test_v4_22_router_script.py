from pathlib import Path

def test_v422_router_script():
    root=Path(__file__).resolve().parents[1]; assert (root/'scripts'/'apply_v4_22_platform_core_router_patch.py').exists()
