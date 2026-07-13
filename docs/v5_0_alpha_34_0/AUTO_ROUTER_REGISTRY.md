# YaSara v5.0-alpha.34.0 — Auto Router Registry

Startup auto-discovery for `backend/app/api/v1/routes/*.py`.

Expected result: route modules exposing `router = APIRouter(...)` are registered automatically, avoiding repeated 404 errors after new sprints.
