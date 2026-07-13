from pathlib import Path

def test_v422_frontend_compatibility_script():
    root=Path(__file__).resolve().parents[2]; p=root/'scripts'/'apply_v4_22_frontend_compatibility_tokens.py'; assert p.exists(); t=p.read_text(encoding='utf-8'); assert 'DeveloperWorkspace' in t and 'WorkspaceButton' in t and 'AI Signals' in t
