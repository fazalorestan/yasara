from pathlib import Path

def test_v500_alpha42_d_path_frontend():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/execution-engine/v5-execution-analytics-types.ts').exists()
