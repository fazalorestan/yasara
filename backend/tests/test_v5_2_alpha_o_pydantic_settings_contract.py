from pathlib import Path

def test_pydantic_settings_contract():
    root = Path(__file__).resolve().parents[2]
    spec = (root / 'packaging/windows/YaSara.spec').read_text(encoding='utf-8')
    build = (root / 'scripts/build_first_real_windows_exe.py').read_text(encoding='utf-8')
    assert 'pydantic_settings' in spec
    assert 'pydantic_settings' in build
    assert '2026.52.O.001' in build
