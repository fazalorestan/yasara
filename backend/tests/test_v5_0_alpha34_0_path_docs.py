from pathlib import Path

def test_v500_alpha34_0_path_docs():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_34_0/AUTO_ROUTER_REGISTRY.md').exists()
