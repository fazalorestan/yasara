# Apply YaSara v4.22.2 Frontend Compatibility Cleanup

Run:

```cmd
cd /d D:\yasara_clean
python scripts\fix_v4_22_2_frontend_compat_cleanup.py
python yasara.py test
python yasara.py start
```

This removes duplicate `WorkspaceButton` declarations and keeps compatibility tokens for old UI tests.
