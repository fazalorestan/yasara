from pathlib import Path

def test_v500_alpha30_router_script():
    root=Path(__file__).resolve().parents[2]; assert (root/'backend'/'scripts'/'apply_v5_0_alpha_30_replay_engine_patch.py').exists()
