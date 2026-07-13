from pathlib import Path

def test_v500_alpha24_router_script():
    root=Path(__file__).resolve().parents[2]; assert (root/'backend'/'scripts'/'apply_v5_0_alpha_24_runtime_api_smoke_patch.py').exists()
