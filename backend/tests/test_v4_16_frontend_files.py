from pathlib import Path
def test_v416_frontend_files():
    root=Path(__file__).resolve().parents[2]
    assert (root/"frontend"/"src"/"api"/"neowaveSprint2.ts").exists()
    assert (root/"frontend"/"src"/"components"/"operational"/"NeoWaveSprint2Status.tsx").exists()
