from pathlib import Path

def test_spec_contains_cryptography():
 text=(Path(__file__).resolve().parents[2]/'packaging/windows/YaSara.spec').read_text(encoding='utf-8')
 assert 'cryptography' in text and 'collect_submodules' in text and 'collect_dynamic_libs' in text
