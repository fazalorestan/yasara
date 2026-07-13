# State Persistence Contract

Future plugins should persist runtime state through Platform Core, not by writing arbitrary files.

## Contract

```text
Plugin
↓
Plugin State Store
↓
Snapshot Export
↓
Restore Contract
```

Current mode is in-memory plus JSON export contract only.
