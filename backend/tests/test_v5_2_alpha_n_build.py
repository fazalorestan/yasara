from pathlib import Path

def test_build():
 text=(Path(__file__).resolve().parents[2]/'scripts/build_first_real_windows_exe.py').read_text(encoding='utf-8')
 assert '2026.52.N.001' in text and 'LEGACY_ACCEPTED_BUILD_IDS' in text and 'apscheduler' in text
