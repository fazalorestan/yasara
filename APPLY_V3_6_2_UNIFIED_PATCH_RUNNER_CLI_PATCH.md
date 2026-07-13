# Apply YaSara v3.6.2 Unified Patch Runner & Project Control CLI

Extract into:

```text
D:\yasara_clean
```

Run from project root:

```cmd
cd /d D:\yasara_clean
python yasara.py patch
```

After this phase, for future patches use:

```cmd
python yasara.py patch
```

Run backend:

```cmd
python yasara.py run-backend
```

Run frontend:

```cmd
python yasara.py run-frontend
```

Test API after backend is running:

```text
http://127.0.0.1:8000/api/v1/v3-6-2/project-cli/summary
```

Adds 6 tests.
