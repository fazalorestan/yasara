# YaSara Verified Release Automation

ترتیب اجرا:

1. `git add --all`
2. `git diff --cached --check`
3. تست کامل پروژه
4. Build فرانت‌اند
5. Build و Validation فایل EXE
6. Dashboard Validation
7. `git commit`
8. `git push`

اگر هر مرحله شکست بخورد، Commit و Push انجام نمی‌شود.

گزارش نهایی:

```text
runtime_reports/release_report.json
```
