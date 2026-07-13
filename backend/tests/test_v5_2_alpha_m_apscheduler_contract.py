from pathlib import Path

def test_apscheduler_contract():
 root=Path(__file__).resolve().parents[2]
 spec=(root/'packaging/windows/YaSara.spec').read_text(encoding='utf-8')
 build=(root/'scripts/build_first_real_windows_exe.py').read_text(encoding='utf-8')
 assert 'apscheduler' in spec and 'apscheduler' in build and '2026.52.M.001' in build
