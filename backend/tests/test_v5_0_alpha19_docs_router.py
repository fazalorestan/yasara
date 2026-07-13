from pathlib import Path

def test_v500_alpha19_docs_router():
    root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_19'/'AUTO_ROUTER_DISCOVERY.md').exists(); assert (root/'backend'/'scripts'/'apply_v5_0_alpha_19_auto_router_patch.py').exists()
