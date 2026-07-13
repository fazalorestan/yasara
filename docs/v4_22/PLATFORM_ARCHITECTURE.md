# YaSara v4.22 Platform Architecture

YaSara evolves into four layers:

```text
Kernel -> Governance -> Platform Services -> Business Plugins
```

Kernel runs the platform and contains no business logic.
Governance owns policy only.
Platform Services are reusable.
Business Plugins remain independent.
