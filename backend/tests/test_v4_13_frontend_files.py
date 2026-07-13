from pathlib import Path
def test_v413_frontend_files():
    root=Path(__file__).resolve().parents[2]
    assert (root/"frontend"/"src"/"api"/"ictEngine.ts").exists()
    assert (root/"frontend"/"src"/"components"/"operational"/"ICTEngineStatus.tsx").exists()
