# Apply YaSara Professional v2.0 Final Release Patch

Extract into:

```text
D:\yasara_clean
```

Then run:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v2_0_final_release_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Build final outputs:

```cmd
cd /d D:\yasara_clean\backend
scripts\build_v2_0_final_release.bat
```

Run app:

```cmd
cd /d D:\yasara_clean\backend
scripts\run_v2_0_final.bat
```

Final progress: 100%
Remaining: 0%

Adds 5 tests.
