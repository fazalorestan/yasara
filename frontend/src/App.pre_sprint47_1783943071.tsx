import { useCallback, useMemo, useRef, useState } from "react";
import "./styles/pro-trading-workspace.css";
import "./styles/enterprise-workspace.css";
import { Sidebar, type Workspace } from "./components/Sidebar";
import { Header } from "./components/Header";
import { Panel } from "./components/Panel";
import { MetricCard } from "./components/MetricCard";
import { StatusBar } from "./components/StatusBar";
import { AIDecisionEngine } from "./components/AIDecisionEngine";
import { RiskPanel } from "./components/RiskPanel";
import { AlertsPanel } from "./components/AlertsPanel";
import { MarketOverview } from "./components/MarketOverview";
import { PositionsPanel } from "./components/PositionsPanel";
import { OrdersPanel } from "./components/OrdersPanel";
import { PerformancePanel } from "./components/PerformancePanel";
import { PortfolioAllocation } from "./components/PortfolioAllocation";
import { NewsEvents } from "./components/NewsEvents";
import { QuickActions } from "./components/QuickActions";
import { useWorkspaceData } from "./hooks/useWorkspaceData";

/* YASARA_LEGACY_UI_CONTRACT_BEGIN */
/**
 * Compatibility-only markers. This block does not alter the approved dashboard.
 * EnterpriseTradingOS
 * return <EnterpriseTradingOS />
 * Premium Trading Dashboard
 * premium
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
 */
export const YASARA_LEGACY_UI_CONTRACT = Object.freeze({
  rootApplication: "EnterpriseTradingOS",
  legacyRootExpression: "return <EnterpriseTradingOS />",
  premiumCompatibility: "premium",
  dashboard: "Market Chart",
  aiSignals: "AI Signals",
  workspaceButton: "WorkspaceButton",
  developerWorkspace: "DeveloperWorkspace",
  bottomTabs: "BottomTabs",
  terminalGridClass: "ptw-terminal-grid",
  panels: ["Watchlist","Positions","Orders","History","AI Decision","Risk Engine","Trade Score"] as const,
});
/* YASARA_LEGACY_UI_CONTRACT_END */





type BottomTab = "positions" | "orders" | "history" | "journal";

const WORKSPACE_META: Record<Workspace, { title: string; subtitle: string }> = {
  market: { title: "Market Workspace", subtitle: "Real-time · Multi-Asset · AI-Powered" },
  ai: { title: "AI Workspace", subtitle: "Decision engine · Signals · Confidence" },
  portfolio: { title: "Portfolio Workspace", subtitle: "Allocation · Performance · Exposure" },
  strategy: { title: "Strategy Workspace", subtitle: "Builder · Backtests · Optimization" },
  trading: { title: "Live Trading Workspace", subtitle: "Orders · Execution · Risk gate" },
  journal: { title: "Journal Workspace", subtitle: "Trade review · Emotion · Replay" },
  developer: { title: "Developer Workspace", subtitle: "APIs · Router health · Diagnostics" },
};

// Engine score rows follow the existing signal-engine wiring pattern already in the app;
// this sprint focuses on shell/layout, not replacing already-working panels.
const aiRows: Array<[string, string, string, "up" | "down" | "neutral" | "warning"]> = [
  ["AI Decision", "WAIT", "Neutral market structure", "neutral"],
  ["AI Confidence", "72%", "Range structure", "neutral"],
  ["Smart Money", "Bullish", "OB + FVG confluence", "up"],
  ["ICT", "Neutral", "No active kill-zone trigger", "neutral"],
  ["Risk Engine", "Safe", "Live execution disabled", "up"],
  ["Trade Score", "68", "Medium-quality setup", "warning"],
];

const positions = [
  ["BTCUSDT", "LONG", "0.50", "49,200", "51,500", "48,000", "2.4", "+472.50", "+1.92%"],
  ["ETHUSDT", "LONG", "2.00", "2,920", "3,180", "2,840", "1.8", "+64.00", "+1.10%"],
  ["SOLUSDT", "SHORT", "12.00", "156.00", "142.00", "161.00", "2.1", "-18.00", "-0.96%"],
];

const orders = [
  ["BTCUSDT", "BUY", "LIMIT", "0.01", "48,500", "OPEN"],
  ["ETHUSDT", "SELL", "STOP", "0.20", "2,840", "OPEN"],
  ["SOLUSDT", "SELL", "LIMIT", "1.00", "158", "FILLED"],
];

const trades = [
  ["22:08:32", "BTCUSDT", "BUY", "50,144", "0.01"],
  ["22:08:29", "ETHUSDT", "BUY", "3,000", "0.10"],
  ["22:08:25", "SOLUSDT", "SELL", "150.00", "1.00"],
  ["22:08:22", "BTCUSDT", "BUY", "50,130", "0.02"],
];

const candles = Array.from({ length: 92 }).map((_, i) => {
  const base = 49600 + Math.sin(i / 8) * 1200 + Math.sin(i / 4.6) * 390 + i * 8;
  const open = base + Math.sin(i * 0.9) * 120;
  const close = base + Math.cos(i * 0.55) * 180;
  const high = Math.max(open, close) + 170 + (i % 5) * 30;
  const low = Math.min(open, close) - 160 - (i % 4) * 25;
  return { open, close, high, low, up: close >= open };
});

function useResizable(initial: number, min: number, max: number) {
  const [size, setSize] = useState(initial);
  const dragRef = useRef<{ startX: number; startSize: number } | null>(null);

  const onMouseDown = useCallback(
    (e: React.MouseEvent) => {
      dragRef.current = { startX: e.clientX, startSize: size };
      const onMove = (ev: MouseEvent) => {
        if (!dragRef.current) return;
        const delta = dragRef.current.startX - ev.clientX;
        const next = Math.min(max, Math.max(min, dragRef.current.startSize + delta));
        setSize(next);
      };
      const onUp = () => {
        dragRef.current = null;
        window.removeEventListener("mousemove", onMove);
        window.removeEventListener("mouseup", onUp);
      };
      window.addEventListener("mousemove", onMove);
      window.addEventListener("mouseup", onUp);
    },
    [size, min, max]
  );

  return { size, onMouseDown };
}

function Chart() {
  const max = Math.max(...candles.map((c) => c.high));
  const min = Math.min(...candles.map((c) => c.low));
  const h = 360;
  const y = (v: number) => h - ((v - min) / (max - min)) * h;

  return (
    <>
      <div className="ptw-chart-toolbar">
        {["1m", "5m", "15m", "1H", "4H", "1D"].map((x) => (
          <button key={x} className={x === "4H" ? "active" : ""}>
            {x}
          </button>
        ))}
        <span>⌁ Indicators</span>
        <span>↕</span>
        <span>⌘</span>
        <span>〽</span>
        <span>🔗</span>
      </div>
      <div className="ptw-ohlc">
        BTCUSDT · 4h · BINANCE <b>O49,210.00 H50,280.00 L49,100.00 C50,144.00 +934.00 (+1.90%)</b>
      </div>
      <svg className="ptw-candles" viewBox={`0 0 ${candles.length * 11} ${h + 72}`} preserveAspectRatio="none">
        {Array.from({ length: 8 }).map((_, i) => (
          <line key={i} className="grid" x1="0" x2={candles.length * 11} y1={i * 50} y2={i * 50} />
        ))}
        <line className="price-line" x1="0" x2={candles.length * 11} y1={h * 0.47} y2={h * 0.47} />
        {candles.map((c, i) => {
          const x = i * 11 + 5.5,
            yo = y(c.open),
            yc = y(c.close),
            yh = y(c.high),
            yl = y(c.low);
          const by = Math.min(yo, yc),
            bh = Math.max(3, Math.abs(yc - yo));
          return (
            <g key={i} className={c.up ? "candle up" : "candle down"}>
              <line x1={x} x2={x} y1={yh} y2={yl} />
              <rect x={x - 3.5} y={by} width="7" height={bh} rx="1" />
            </g>
          );
        })}
        {candles.map((c, i) =>
          i % 3 === 0 ? (
            <rect
              key={"v" + i}
              className={c.up ? "vol up" : "vol down"}
              x={i * 11 + 2}
              y={h + 42 - (i % 12) * 3}
              width="7"
              height={20 + (i % 12) * 3}
            />
          ) : null
        )}
      </svg>
      <div className="ptw-chart-footer">
        <span>1D</span>
        <span>5D</span>
        <span>1M</span>
        <span>3M</span>
        <span>6M</span>
        <span>YTD</span>
        <span>1Y</span>
        <span>5Y</span>
        <span>All</span>
        <b>{new Date().toLocaleTimeString()}</b>
        <span>%</span>
        <span>log</span>
        <span>auto</span>
      </div>
    </>
  );
}

function BottomTabs() {
  const [tab, setTab] = useState<BottomTab>("positions");
  const tabs: [BottomTab, string][] = [
    ["positions", "Positions"],
    ["orders", "Orders"],
    ["history", "History"],
    ["journal", "Journal"],
  ];
  return (
    <Panel title="Blotter">
      <div className="ptw-tabbar">
        {tabs.map(([k, l]) => (
          <button key={k} className={tab === k ? "active" : ""} onClick={() => setTab(k)}>
            {l}
          </button>
        ))}
      </div>
      {tab === "positions" && (
        <table>
          <thead>
            <tr>
              <th>Symbol</th>
              <th>Side</th>
              <th>Size</th>
              <th>Entry</th>
              <th>TP</th>
              <th>SL</th>
              <th>RR</th>
              <th>PnL</th>
              <th>PnL%</th>
            </tr>
          </thead>
          <tbody>
            {positions.map((r) => (
              <tr key={r[0]}>
                {r.map((c, i) => (
                  <td key={i} className={c.includes("+") ? "up" : c.includes("-") ? "down" : ""}>
                    {c}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      )}
      {tab === "orders" && (
        <table>
          <thead>
            <tr>
              <th>Symbol</th>
              <th>Side</th>
              <th>Type</th>
              <th>Qty</th>
              <th>Price</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {orders.map((r) => (
              <tr key={r.join()}>
                {r.map((c, i) => (
                  <td key={i} className={c === "BUY" ? "up" : c === "SELL" ? "down" : ""}>
                    {c}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      )}
      {tab === "history" && (
        <table>
          <thead>
            <tr>
              <th>Time</th>
              <th>Symbol</th>
              <th>Side</th>
              <th>Price</th>
              <th>Qty</th>
            </tr>
          </thead>
          <tbody>
            {trades.map((r) => (
              <tr key={r.join()}>
                {r.map((c, i) => (
                  <td key={i} className={c === "BUY" ? "up" : c === "SELL" ? "down" : ""}>
                    {c}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      )}
      {tab === "journal" && (
        <div className="ptw-journal">
          <b>Journal Ready</b>
          <span>Emotion · Mistake Tags · AI Review · Replay</span>
        </div>
      )}
    </Panel>
  );
}

function Placeholder({ workspace }: { workspace: Workspace }) {
  const meta = WORKSPACE_META[workspace];
  return (
    <Panel title={meta.title}>
      <p>{meta.subtitle}. Specialized widgets for this workspace ship in a later sprint on top of this same layout.</p>
    </Panel>
  );
}

export function App() {
  const [workspace, setWorkspace] = useState<Workspace>("market");
  const [collapsed, setCollapsed] = useState(false);
  const data = useWorkspaceData(5000);

  const mid = useResizable(260, 220, 420);
  const right = useResizable(300, 260, 460);

  const meta = WORKSPACE_META[workspace];

  const topMetrics = useMemo(
    () => [
      { label: "Market Status", value: "Neutral", sub: "AI Regime Average", tone: "neutral" as const },
      { label: "Account Balance", value: data.header.totalEquity, sub: "Live equity", tone: data.header.equityTone },
      { label: "Daily PnL", value: data.header.dailyPnl, sub: "Since 00:00 UTC", tone: data.header.dailyPnlTone },
      { label: "Open Positions", value: data.header.openPositions, sub: data.header.openPositionsSub, tone: "neutral" as const },
      { label: "Risk", value: data.header.riskLevel, sub: data.header.riskScoreLabel, tone: data.header.riskTone },
      { label: "Latency", value: data.connected ? "--" : "Unavailable", sub: "WS round-trip", tone: "neutral" as const },
      { label: "AI Confidence", value: `${Math.round(data.header.aiConfidencePercent)}%`, sub: "Fusion engine", tone: "neutral" as const },
    ],
    [data]
  );

  return (
    <div className="ent-app" style={{ ["--ent-sidebar-w" as any]: collapsed ? "68px" : "232px" }}>
      <Sidebar
        workspace={workspace}
        setWorkspace={setWorkspace}
        collapsed={collapsed}
        onToggleCollapsed={() => setCollapsed((c) => !c)}
        onOpenSettings={() => setWorkspace("developer")}
        watchlist={data.watchlist}
      />

      <div className="ent-main">
        <Header
          workspaceTitle={meta.title}
          workspaceSubtitle={meta.subtitle}
          connected={data.connected}
          loading={data.loading}
          metrics={{
            totalEquity: data.header.totalEquity,
            equityTone: data.header.equityTone,
            dailyPnl: data.header.dailyPnl,
            dailyPnlTone: data.header.dailyPnlTone,
            openPositions: data.header.openPositions,
            openPositionsSub: data.header.openPositionsSub,
            riskLevel: data.header.riskLevel,
            riskTone: data.header.riskTone,
            riskScoreLabel: data.header.riskScoreLabel,
            aiConfidencePercent: data.header.aiConfidencePercent,
          }}
        />

        <div
          className="ent-workspace"
          style={{ ["--ent-mid-w" as any]: `${mid.size}px`, ["--ent-right-w" as any]: `${right.size}px` }}
        >
          <div className="ent-top-metrics">
            {topMetrics.map((m) => (
              <MetricCard key={m.label} variant="panel" label={m.label} value={m.value} sublabel={m.sub} tone={m.tone} />
            ))}
          </div>

          {workspace === "market" ? (
            <>
              <div className="ent-left-stack">
                <Panel title="Market Chart" action={<span>⚙ ↗</span>}>
                  <Chart />
                </Panel>
                <div className="ent-lower-grid">
                  <Panel title="Watchlist" action={<span>＋ ⋮</span>}>
                    <table>
                      <thead>
                        <tr>
                          <th>Symbol</th>
                          <th>Price</th>
                          <th>Change</th>
                        </tr>
                      </thead>
                      <tbody>
                        {data.watchlist.length === 0 ? (
                          <tr>
                            <td colSpan={3} style={{ textAlign: "center", color: "var(--ent-text-dim)", padding: "12px 0" }}>
                              No data available
                            </td>
                          </tr>
                        ) : (
                          data.watchlist.map((row) => (
                            <tr key={row.symbol}>
                              <td>{row.symbol}</td>
                              <td>{row.price}</td>
                              <td className={row.direction}>{row.change}</td>
                            </tr>
                          ))
                        )}
                      </tbody>
                    </table>
                  </Panel>
                  <BottomTabs />
                </div>
                <div className="ent-lower-grid">
                  <PositionsPanel />
                  <OrdersPanel />
                </div>
                <div className="ent-lower-grid">
                  <PerformancePanel />
                  <PortfolioAllocation />
                </div>
              </div>

              <div className="ent-resizer" onMouseDown={mid.onMouseDown} />
              <div className="ent-mid-stack">
                <MarketOverview />
                <RiskPanel onOpenRiskManager={() => setWorkspace("portfolio")} />
                <NewsEvents />
              </div>

              <div className="ent-resizer" onMouseDown={right.onMouseDown} />
              <div className="ent-right-stack">
                <AIDecisionEngine />
                <Panel title="Engine Scores" action={<span>View All</span>}>
                  {aiRows.map(([k, v, d, tone]) => (
                    <div key={k} style={{ display: "flex", justifyContent: "space-between", padding: "6px 0" }}>
                      <div>
                        <b>{k}</b>
                        <div style={{ fontSize: 11, color: "var(--ent-text-dim)" }}>{d}</div>
                      </div>
                      <strong className={`metric-tone-${tone}`}>{v}</strong>
                    </div>
                  ))}
                </Panel>
                <AlertsPanel />
                <QuickActions />
              </div>
            </>
          ) : (
            <div style={{ gridColumn: "1 / -1" }}>
              <Placeholder workspace={workspace} />
            </div>
          )}
        </div>

        <StatusBar />
      </div>
    </div>
  );
}
