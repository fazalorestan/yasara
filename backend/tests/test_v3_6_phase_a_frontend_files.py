from pathlib import Path

def test_v36_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "phaseAMetaYkb.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "PhaseAMetaYkbStatus.tsx").exists()
