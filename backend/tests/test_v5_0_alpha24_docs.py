from pathlib import Path

def test_v500_alpha24_docs():
    root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_24'/'RUNTIME_API_SMOKE_TEST.md').exists()
