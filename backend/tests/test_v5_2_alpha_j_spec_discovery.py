from pathlib import Path

def test_spec_discovery():
 text=(Path(__file__).resolve().parents[2]/'packaging/windows/YaSara.spec').read_text(encoding='utf-8')
 assert 'collect_submodules' in text and 'copy_metadata' in text and ('requirements.txt' in text or 'discover_import_roots' in text)
