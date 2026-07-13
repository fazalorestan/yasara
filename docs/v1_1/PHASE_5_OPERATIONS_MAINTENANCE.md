# YaSara Professional v1.1 — Phase 5: Operations & Maintenance Layer

This phase adds project maintenance utilities and operational checks.

## Added

- `backend/scripts/cleanup_project.bat`
- `backend/scripts/project_health_check.py`
- `backend/scripts/project_info.py`
- `backend/scripts/verify_release.py`

## Cleanup

Safe mode:

```cmd
backend\scripts\cleanup_project.bat
```

Deep mode:

```cmd
backend\scripts\cleanup_project.bat --deep
```

## Safety

Maintenance only. No trading and no market execution logic.
