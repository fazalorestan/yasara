from pathlib import Path

def test_v500_alpha30_docs():
    root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_30'/'REPLAY_ENGINE_FOUNDATION.md').exists()
