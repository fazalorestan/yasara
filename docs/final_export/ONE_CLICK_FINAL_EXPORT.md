# One-Click Final Export

Run:

```cmd
cd /d D:\yasara\yasara\backend
python scripts\apply_one_click_final_export_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
scripts\one_click_final_export.bat
```

Output:

`D:\yasara\yasara\yasara_professional_v1_0_stable.zip`
