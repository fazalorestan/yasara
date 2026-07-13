from pathlib import Path
def test_v417_frontend_files():
    root=Path(__file__).resolve().parents[2]
    assert (root/"frontend"/"src"/"api"/"elliott.ts").exists()
    assert (root/"frontend"/"src"/"components"/"operational"/"ElliottStatus.tsx").exists()
