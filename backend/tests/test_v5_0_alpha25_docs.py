from pathlib import Path

def test_v500_alpha25_docs():
    root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_25'/'SELF_HEALING_PATCH_PIPELINE.md').exists()
