from pathlib import Path
def test_v415_frontend_files():
    root=Path(__file__).resolve().parents[2]
    assert (root/"frontend"/"src"/"api"/"neowave.ts").exists()
    assert (root/"frontend"/"src"/"components"/"operational"/"NeoWaveStatus.tsx").exists()
