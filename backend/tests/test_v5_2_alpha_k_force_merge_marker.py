from pathlib import Path

def test_force_merge_k_marker():
 text=(Path(__file__).resolve().parents[2]/'scripts/build_first_real_windows_exe.py').read_text(encoding='utf-8')
 assert ('2026.52.L.001' in text or '2026.52.N.001' in text) and 'discover_import_roots' in text and 'sqlalchemy' in text
