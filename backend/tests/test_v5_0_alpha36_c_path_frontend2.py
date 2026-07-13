from pathlib import Path

def test_v500_alpha36_c_path_frontend2():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/plugin-sdk/v5-plugin-versioning-types.ts').exists()
