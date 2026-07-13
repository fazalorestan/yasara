from pathlib import Path
def test_v362_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "projectCli.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "ProjectCliStatus.tsx").exists()
