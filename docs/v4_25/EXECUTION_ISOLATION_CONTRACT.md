# Execution Isolation Contract

Analysis engines must never know whether live execution exists.

```text
Analysis Engine
  ↓ produces analysis result
Policy Gate
  ↓ validates permission/license/feature flag/risk
Execution Adapter
```

This Sprint defines the contract only. It does not enable live execution.
