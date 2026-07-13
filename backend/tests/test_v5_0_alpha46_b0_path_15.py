from pathlib import Path

def test_path_15():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/stabilization/v5-core-stabilization-types.ts').exists()
