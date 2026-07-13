from pathlib import Path

def test_v500_alpha34_0_path_apply_doc():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_34_0_AUTO_ROUTER_REGISTRY_PATCH.md').exists()
