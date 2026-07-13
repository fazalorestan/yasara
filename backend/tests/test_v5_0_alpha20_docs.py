from pathlib import Path

def test_v500_alpha20_docs():
    root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_20'/'LAUNCHER_SWAGGER_API_SEARCH.md').exists()
