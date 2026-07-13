from pathlib import Path

def test_compile_validation_script_exists():
    root = Path(__file__).resolve().parents[2]
    text = (root / "scripts/validate_python_compile.py").read_text(encoding="utf-8")
    assert "py_compile.compile" in text
    assert "backend/app" in text
