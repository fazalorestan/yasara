# YaSara v5.0-alpha.17.1 — API Health Visibility Hotfix

Fix API router visibility behavior when an explicit empty route list is provided.

Correct behavior:
- `routes=None`: use expected catalog for internal self-check.
- `routes=[]`: treat as no routes available and return missing endpoints.

Hotfix only. No dashboard change. No auto trading.
