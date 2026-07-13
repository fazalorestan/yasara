# YaSara Data Flow

```text
Exchange
  → Raw Market Data
  → Normalizer
  → Market Data Engine
  → Live Exchange Foundation
  → Indicator Engine
  → Market Analysis Engine
  → Smart Money Engine
  → Strategy Builder
  → AI Engine
  → Risk Engine
  → Signal Engine
  → Notification / Telegram / Dashboard
```

Personal-only path:

```text
Signal → Risk Gate → Execution Engine → Bitunix → Position Sync → Journal/YKB
```

Commercial path:

```text
Signal → Risk Explanation → Dashboard/Notifications
```

Commercial build must not include Execution Engine.
