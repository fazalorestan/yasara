# YaSara System Architecture

## High-Level Modules

```text
Clients
  ├─ Flutter Desktop
  ├─ Flutter Mobile
  └─ Future Web

Backend API
  ├─ Auth & Users
  ├─ Market Data
  ├─ Intelligence
  ├─ Decision
  ├─ Risk
  ├─ Backtesting
  ├─ AI
  ├─ Notifications
  └─ Trading Execution

Infrastructure
  ├─ PostgreSQL
  ├─ Redis / future cache
  ├─ Docker
  ├─ CI/CD
  └─ Monitoring
```

## Sprint 1 Focus

```text
Binance REST/WebSocket
    ↓
Raw Exchange Response
    ↓
Adapter Normalization
    ↓
Market Data Models
    ↓
Storage / Cache
    ↓
API
    ↓
Flutter UI
```
