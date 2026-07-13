# Apply Sprint 46

```cmd
cd /d D:\yasara_clean
python yasara.py patch
python scripts\force_repair_sprint45_2.py
python scripts\validate_dashboard_stability.py
python scripts\validate_python_compile.py
python yasara.py test

cd frontend
npm run build
cd ..

python scripts\build_first_real_windows_exe.py --execute
python scripts\finalize_sprint46_and_launch_dashboard.py
```
