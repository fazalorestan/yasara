from pathlib import Path

def test_path_11():
 root=Path(__file__).resolve().parents[2]; assert (root/"frontend/src/desktop-app/v5-desktop-foundation-types.ts").exists()
