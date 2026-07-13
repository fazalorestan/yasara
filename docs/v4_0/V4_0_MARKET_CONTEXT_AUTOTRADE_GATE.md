# YaSara v4.0 — Market Context Engine + Personal Auto-Trade Gate

## Constitution Compliance
- No feature removed.
- No existing API broken.
- No architecture rewrite.
- Execution Engine is still not implemented.
- Auto-trade is Personal-only and disabled unless gate passes.
- Commercial build must exclude execution_engine and trade API access.

## Added
- Market Context Engine
- Engine Registry
- Confidence Normalizer
- Multi-Timeframe Context
- Personal Auto-Trade Gate
- Frontend Auto-Trade status component

## Safety
This phase does not send real orders. It only prepares the gated permission layer.
