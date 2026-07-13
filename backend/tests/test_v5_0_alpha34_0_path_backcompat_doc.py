from pathlib import Path

def test_v500_alpha34_0_path_backcompat_doc():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_34_0_AUTO_ROUTER_REGISTRY_BACKWARD_COMPATIBILITY.md').exists()
