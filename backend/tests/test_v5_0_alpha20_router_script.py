from pathlib import Path

def test_v500_alpha20_router_script():
    root=Path(__file__).resolve().parents[2]; assert (root/'backend'/'scripts'/'apply_v5_0_alpha_20_launcher_api_search_patch.py').exists()
