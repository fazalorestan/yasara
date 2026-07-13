# Apply YaSara v1.1 Final Windows & Mobile Output Patch

Extract into your current YaSara project root:

`D:\yasara_clean`

Then run:

```cmd
cd /d D:\yasara_clean\backend
python scripts\apply_v1_1_final_distribution_router_patch.py
set PYTHONPATH=%CD%
python -m pytest tests
```

Adds 4 tests.

To build both outputs:

```cmd
cd /d D:\yasara_clean\backend
scripts\build_all_outputs_v1_1.bat
```
