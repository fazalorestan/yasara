from pathlib import Path
def test_v414_frontend_files():
    root=Path(__file__).resolve().parents[2]
    assert (root/"frontend"/"src"/"api"/"aiFusion.ts").exists()
    assert (root/"frontend"/"src"/"components"/"operational"/"AIFusionStatus.tsx").exists()
