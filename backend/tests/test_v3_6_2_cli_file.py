from pathlib import Path
def test_v362_cli_file_exists():
    root = Path(__file__).resolve().parents[2]
    cli = root / "yasara.py"
    assert cli.exists()
    text = cli.read_text(encoding="utf-8")
    assert "def patch" in text
    assert "def run_backend" in text
