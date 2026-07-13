# Apply YaSara v4.22.1 Frontend Literal Newline Fix

Run:

```cmd
cd /d D:\yasara_clean
python scripts\fix_v4_22_frontend_literal_newlines.py
python yasara.py test
python yasara.py start
```

This fixes raw `\n` characters in `frontend/src/App.tsx`.
