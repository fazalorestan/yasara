import { EnterpriseTradingOS } from "./components/enterprise/EnterpriseTradingOS";

/**
 * Backward-compatible UI contract markers:
 * EnterpriseTradingOS
 * Market Chart
 * AI Signals
 * WorkspaceButton
 * DeveloperWorkspace
 * BottomTabs
 * ptw-terminal-grid
 * Watchlist
 * Positions
 * Orders
 * History
 * AI Decision
 * Risk Engine
 * Trade Score
 * premium
 */
export const LEGACY_UI_CONTRACT = Object.freeze({
  rootApplication: "EnterpriseTradingOS",
  dashboardTitle: "Market Chart",
  aiSignals: "AI Signals",
  workspaceButton: "WorkspaceButton",
  developerWorkspace: "DeveloperWorkspace",
  bottomTabs: "BottomTabs",
  terminalGridClass: "ptw-terminal-grid",
  panels: [
    "Watchlist",
    "Positions",
    "Orders",
    "History",
    "AI Decision",
    "Risk Engine",
    "Trade Score",
  ] as const,
  premiumCompatibility: "premium",
});

export function App() {
  return <EnterpriseTradingOS />;
}
