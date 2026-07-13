# Plugin Sandbox Rules

A plugin should not crash the platform.

## Lifecycle

```text
Created
↓
Started
↓
Running
↓
Warning/Error
↓
Recovering
↓
Paused/Disabled
↓
Stopped
```

## Current Mode

Report-only. No plugin is actually isolated into a separate process yet.
