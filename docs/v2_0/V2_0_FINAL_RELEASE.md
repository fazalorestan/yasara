# YaSara Professional v2.0 Final Release

Progress: 100%
Remaining: 0%

## Build

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v2_0_final_release_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
scripts\build_v2_0_final_release.bat
```

## Run

```cmd
cd /d D:\yasara_clean\backend
scripts\run_v2_0_final.bat
```
