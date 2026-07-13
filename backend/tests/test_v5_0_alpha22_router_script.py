from pathlib import Path

def test_v500_alpha22_router_script():
    root=Path(__file__).resolve().parents[2]; assert (root/'backend'/'scripts'/'apply_v5_0_alpha_22_broker_layer_patch.py').exists()
