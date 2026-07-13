from pathlib import Path

def test_spec_contains_staticfiles():
 text=(Path(__file__).resolve().parents[2]/'packaging/windows/YaSara.spec').read_text(encoding='utf-8')
 assert 'collect_submodules' in text and 'fastapi' in text and 'starlette' in text
