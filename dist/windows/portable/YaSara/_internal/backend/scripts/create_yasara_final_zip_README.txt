Final manual export recommendation:

1. cd /d D:\yasara\yasara\backend
2. set PYTHONPATH=%CD%
3. python -m pytest tests
4. scripts\safe_consolidation_cleanup.bat
5. cd /d D:\yasara\yasara
6. Create ZIP:
   yasara_professional_v1_0_stable.zip

Include:
- backend
- docs
- deployment
- README.md
- CHANGELOG.md

Do not include:
- .venv
- __pycache__
- .pytest_cache
- build
- dist
