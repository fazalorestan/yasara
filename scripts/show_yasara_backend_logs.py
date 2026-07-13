from pathlib import Path
for name in ['backend_stdout.log','backend_stderr.log','launcher_report.json']:
    p=Path('dist/windows/portable/YaSara/runtime_reports')/name
    print('\n---',p,'---')
    print(p.read_text(encoding='utf-8',errors='replace') if p.exists() else 'MISSING')
