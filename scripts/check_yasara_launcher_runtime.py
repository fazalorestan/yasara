from pathlib import Path
import json

def main():
    report = Path('dist/windows/portable/YaSara/runtime_reports/launcher_report.json')
    print('REPORT:', report)
    print('EXISTS:', report.exists())
    if report.exists():
        text = report.read_text(encoding='utf-8')
        print(text)
        data = json.loads(text)
        ok = data.get('started') and data.get('auto_trading_enabled') is False
        return 0 if ok else 2
    return 1
if __name__ == '__main__': raise SystemExit(main())
