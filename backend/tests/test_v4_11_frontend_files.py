from pathlib import Path
def test_v411_frontend_files():
    root=Path(__file__).resolve().parents[2]
    assert (root/"frontend"/"src"/"api"/"smartMoneyPro.ts").exists()
    assert (root/"frontend"/"src"/"components"/"operational"/"SmartMoneyProStatus.tsx").exists()
