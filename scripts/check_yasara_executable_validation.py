from pathlib import Path
import json
p=Path('dist/windows/reports/build_report.json')
print(p.read_text(encoding='utf-8') if p.exists() else 'MISSING')
if p.exists():
    data=json.loads(p.read_text(encoding='utf-8'))
    raise SystemExit(0 if data.get('executable_validation',{}).get('ready') else 1)
raise SystemExit(1)
