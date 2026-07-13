# Governance Bridge

The Governance Bridge evaluates whether a plugin is allowed to run.

Evaluation order:

```text
Plugin Manifest
↓
Required Permissions
↓
Required Licenses
↓
Feature Flags
↓
Result
```

This Sprint only prepares the contract. It does not block current modules yet.
