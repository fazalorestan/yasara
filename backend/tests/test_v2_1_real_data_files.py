from pathlib import Path

def test_real_data_files_exist():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "realData.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "OperationalStatus.tsx").exists()
