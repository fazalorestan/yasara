from pathlib import Path

def test_v500_alpha27_docs():
    root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_27'/'SCANNER_FOUNDATION.md').exists()
