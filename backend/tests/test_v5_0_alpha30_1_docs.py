from pathlib import Path

def test_v500_alpha30_1_docs():
    root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_30_1'/'ROUTER_AUTO_REGISTRATION.md').exists()
