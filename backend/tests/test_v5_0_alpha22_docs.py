from pathlib import Path

def test_v500_alpha22_docs():
    root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_22'/'BROKER_LAYER_FOUNDATION.md').exists()
