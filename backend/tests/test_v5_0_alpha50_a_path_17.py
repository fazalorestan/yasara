from pathlib import Path

def test_path_17():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/windows-app/v5-windows-real-exe-types.ts').exists()
