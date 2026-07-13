from pathlib import Path

def test_v500_alpha36_d_path_frontend():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/plugin-sdk/v5-plugin-enterprise-types.ts').exists()
