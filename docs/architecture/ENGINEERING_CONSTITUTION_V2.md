# YaSara Engineering Constitution v2

## Non-Negotiable Rules
- Do not mix UI and business logic.
- Backend owns business logic.
- Flutter owns presentation.
- Exchange adapters must isolate exchange-specific formats.
- Every output must be explainable.
- No live trading without Risk Engine, Paper Trading, Audit Logging and Emergency Stop.
- Prefer modular services over monolith modules.
- Every module must be testable.
- Every public API must have schemas.
- Every schema must be version-safe.
- Every migration must be reversible where possible.
- Secrets must never be committed.

## Architecture Principles
- Clean Architecture
- SOLID
- Async-first backend
- PostgreSQL-first production design
- SQLite only for local demo/testing
- Event-driven where useful
- Adapter pattern for exchanges
- Repository pattern for persistence
- Service layer for business logic

## Safety Principles
- Capital protection before profit.
- No Trade is better than a bad trade.
- AI estimates probability; it does not predict markets.
- Every decision must explain WHY.
