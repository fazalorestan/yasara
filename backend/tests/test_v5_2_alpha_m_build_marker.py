from pathlib import Path

def test_build_marker():
 text=(Path(__file__).resolve().parents[2]/'scripts/build_first_real_windows_exe.py').read_text(encoding='utf-8')
 assert '2026.52.M.001' in text and 'apscheduler' in text and 'ALWAYS_VALIDATE' in text
