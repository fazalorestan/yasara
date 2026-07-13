import { Panel } from "./Panel";
import "../styles/enterprise-panels.css";

/**
 * Portfolio Allocation panel.
 *
 * There is currently no backend endpoint that returns per-asset
 * allocation weights (checked: paper-trading account/summary, risk-engine
 * summary, ai-fusion summary, notifications, real-data watchlist/
 * market-snapshot, final-operational, risk/backtest/paper-state).
 * Deriving percentages from position size * entry price would be an
 * approximation not actually returned by the backend, which is exactly
 * the kind of fabricated business value this pass is meant to eliminate.
 *
 * Per "Do NOT create new API endpoints" / "Do NOT fabricate values",
 * this widget honestly renders Unavailable until a real allocation
 * endpoint exists, rather than guessing.
 */
export function PortfolioAllocation() {
  return (
    <Panel title="Portfolio Allocation">
      <div className="ent-empty">Unavailable</div>
    </Panel>
  );
}
