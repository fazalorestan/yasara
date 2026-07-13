from pathlib import Path

def test_launcher():
 text=(Path(__file__).resolve().parents[2]/'desktop/yasara_desktop.py').read_text(encoding='utf-8')
 assert '2026.52.N.001' in text and 'dump_thread_diagnostics' in text and 'faulthandler' in text
