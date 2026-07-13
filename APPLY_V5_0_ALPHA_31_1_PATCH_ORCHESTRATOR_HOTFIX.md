# Apply YaSara v5.0-alpha.31.1 Patch Orchestrator Hotfix

Run once manually:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v5_0_alpha_31_1_patch_orchestrator_hotfix.py
```

Then:

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python yasara.py test
python yasara.py run-backend
```

API:

```cmd
curl http://127.0.0.1:8000/api/v1/v5-0-alpha-31-1/patch-orchestrator/summary
```
