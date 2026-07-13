# Apply Critical Review Route Fix v2

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py run-backend
```

Test:

```cmd
curl http://127.0.0.1:8000/api/v1/v5-0-alpha-47/critical-review/summary
```
