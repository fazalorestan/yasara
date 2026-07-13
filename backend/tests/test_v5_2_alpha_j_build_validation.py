from pathlib import Path

def test_build_validation():
 text=(Path(__file__).resolve().parents[2]/'scripts/build_first_real_windows_exe.py').read_text(encoding='utf-8')
 assert 'validate_dependencies' in text and 'validate_executable' in text and 'health_ok' in text
