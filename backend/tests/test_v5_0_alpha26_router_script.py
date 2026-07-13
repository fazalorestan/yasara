from pathlib import Path

def test_v500_alpha26_router_script():
    root=Path(__file__).resolve().parents[2]; assert (root/'backend'/'scripts'/'apply_v5_0_alpha_26_portfolio_manager_patch.py').exists()
