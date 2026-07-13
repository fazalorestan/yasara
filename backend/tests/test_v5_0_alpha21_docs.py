from pathlib import Path

def test_v500_alpha21_docs():
    root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_21'/'PATCH_PIPELINE_AUTODISCOVERY.md').exists()
