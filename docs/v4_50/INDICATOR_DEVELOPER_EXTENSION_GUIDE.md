# Indicator Developer Extension Guide

Future indicators should follow the same structure as YaSara:

```text
indicator manifest
runtime adapter
chart overlay contract
engine bridge
scanner contract
alert contract
settings presets
readiness gate
```

Rules:
- Never couple an indicator directly to live execution.
- Runtime output must remain analysis-only.
- Chart rendering must consume contracts, not raw strategy logic.
- Scanner, alerts and AI panels consume normalized output.
