from pathlib import Path

def test_launcher_build_sync():
 root=Path(__file__).resolve().parents[2]
 launcher=(root/'desktop/yasara_desktop.py').read_text(encoding='utf-8')
 build=(root/'scripts/build_first_real_windows_exe.py').read_text(encoding='utf-8')
 assert '2026.52.N.001' in launcher and '2026.52.N.001' in build and 'dump_thread_diagnostics' in launcher
