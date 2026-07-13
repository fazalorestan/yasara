param(
    [string]$ComposeFile = "deployment/docker/docker-compose.production.yml"
)

Write-Host "Starting YaSara production deployment..."
docker compose -f $ComposeFile up -d --build
Write-Host "Deployment started. Check health at http://127.0.0.1:8000/health"
