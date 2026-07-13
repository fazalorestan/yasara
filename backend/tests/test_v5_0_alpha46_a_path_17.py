from pathlib import Path

def test_path_17():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/desktop-app/v5-desktop-host-types.ts').exists()
