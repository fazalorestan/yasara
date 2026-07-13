from pathlib import Path

def test_spec_marker():
 text=(Path(__file__).resolve().parents[2]/'packaging/windows/YaSara.spec').read_text(encoding='utf-8')
 assert 'apscheduler' in text and 'collect_submodules' in text and 'requirements.txt' in text
