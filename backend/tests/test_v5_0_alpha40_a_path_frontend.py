from pathlib import Path

def test_v500_alpha40_a_path_frontend():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/ai-intelligence/v5-ai-core-types.ts').exists()
