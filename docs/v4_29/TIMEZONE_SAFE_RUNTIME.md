# YaSara v4.29 — Platform Warning Cleanup & Timezone-Safe Runtime

## Goal
Remove deprecated `datetime.utcnow()` usage from Platform Core runtime infrastructure and standardize UTC timestamps.

## Scope
- Infrastructure quality only
- No trading feature
- No dashboard change
- No API breaking change

## Adds
- Platform Clock Service
- UTC ISO timestamp helper
- Audit Log timezone-safe timestamp
- Event Bus timezone-safe timestamp
- State Snapshot timezone-safe timestamp
- Backward-compatible timestamp strings
