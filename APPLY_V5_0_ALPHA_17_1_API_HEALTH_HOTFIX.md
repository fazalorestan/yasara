# Apply YaSara v5.0-alpha.17.1 API Health Visibility Hotfix

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py start
```

Expected:
- Previous failing test passes.
- 4 new hotfix tests are added.
