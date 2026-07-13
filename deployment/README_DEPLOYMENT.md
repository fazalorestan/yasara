# YaSara Sprint 18 Deployment

## Local production-like deployment

```powershell
cd yasara_sprint18_deployment_beta_performance_v1
powershell -ExecutionPolicy Bypass -File deployment/scripts/deploy_windows.ps1
```

## Health

- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/docs`

## Release readiness

- `GET /api/v1/release-v1/readiness`
