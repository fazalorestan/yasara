# Apply YaSara v2.7 Final Installer & Distribution Patch

Extract into:

```text
D:\yasara_clean
```

Apply router and test:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v2_7_distribution_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Build final outputs:

```cmd
cd /d D:\yasara_clean\backend
scripts\build_v2_7_final_distribution.bat
```

Run final app:

```cmd
cd /d D:\yasara_clean\backend
scripts\run_yasara_v2_7.bat
```

Create desktop shortcut:

```cmd
cd /d D:\yasara_clean\backend
scripts\create_v2_7_desktop_shortcut.bat
```

Test API:

```text
http://127.0.0.1:8000/api/v1/v2-7/distribution/summary
```

Adds 7 tests.
