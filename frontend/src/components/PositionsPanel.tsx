import { Plus } from "lucide-react";
import { Panel } from "./Panel";
import { useResilientResource } from "../hooks/useResilientResource";
import { getPaperTradingV45Account } from "../api/paperTradingV45";
import "../styles/enterprise-panels.css";

export interface PositionRow {
  symbol: string;
  side: "LONG" | "SHORT";
  size: string;
  entryPrice: string;
  pnl: number;
  pnlPercent: number;
}

interface PositionsSnapshot {
  totalEquity: string | null;
  unrealizedPnl: number | null;
  unrealizedPnlPercent: number | null;
  rows: PositionRow[];
}

async function fetchPositions(): Promise<PositionsSnapshot | null> {
  const res: any = await getPaperTradingV45Account();
  const positions = res?.positions;
  if (!Array.isArray(positions)) return null;

  return {
    totalEquity: res?.equity != null ? `$${Number(res.equity).toLocaleString()}` : null,
    unrealizedPnl: typeof res?.unrealized_pnl === "number" ? res.unrealized_pnl : null,
    unrealizedPnlPercent: typeof res?.unrealized_pnl_percent === "number" ? res.unrealized_pnl_percent : null,
    rows: positions.map((p: any) => ({
      symbol: p.symbol ?? "--",
      side: (p.side ?? (p.size >= 0 ? "LONG" : "SHORT")).toUpperCase(),
      size: p.size != null ? String(p.size) : "--",
      entryPrice: p.entry_price != null ? Number(p.entry_price).toLocaleString() : "--",
      pnl: typeof p.pnl === "number" ? p.pnl : 0,
      pnlPercent: typeof p.pnl_percent === "number" ? p.pnl_percent : 0,
    })),
  };
}

/**
 * Positions panel. Self-fetches from the existing paper-trading account
 * endpoint via the shared resilient hook. Shows "Unavailable" if the
 * endpoint never responds, and "No data available" if the account has
 * zero open positions - never fabricated rows or totals.
 */
export function PositionsPanel({ onViewAll, onNewOrder }: { onViewAll?: () => void; onNewOrder?: () => void }) {
  const res = useResilientResource<PositionsSnapshot>(fetchPositions, { baseIntervalMs: 6000 });
  const d = res.data;
  const count = d?.rows.length ?? 0;

  return (
    <Panel
      title={`Positions${res.available ? ` (${count})` : ""}`}
      action={<span onClick={onViewAll} style={{ cursor: "pointer" }}>View All</span>}
    >
      {!res.available ? (
        <div className="ent-empty">Unavailable</div>
      ) : (
        <>
          <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 10, fontSize: 12 }}>
            <div>
              <div style={{ color: "var(--ent-text-dim)", fontSize: 10.5, textTransform: "uppercase" }}>Total Equity</div>
              <strong style={{ fontSize: 14 }}>{d?.totalEquity ?? "Unavailable"}</strong>
            </div>
            <div style={{ textAlign: "right" }}>
              <div style={{ color: "var(--ent-text-dim)", fontSize: 10.5, textTransform: "uppercase" }}>Unrealized PnL</div>
              <strong className={d && d.unrealizedPnl != null && d.unrealizedPnl >= 0 ? "metric-tone-up" : "metric-tone-down"} style={{ fontSize: 14 }}>
                {d?.unrealizedPnl != null
                  ? `${d.unrealizedPnl >= 0 ? "+" : ""}${d.unrealizedPnl.toLocaleString()}${
                      d.unrealizedPnlPercent != null ? ` (${d.unrealizedPnlPercent >= 0 ? "+" : ""}${d.unrealizedPnlPercent.toFixed(2)}%)` : ""
                    }`
                  : "Unavailable"}
              </strong>
            </div>
          </div>

          {count === 0 ? (
            <div className="ent-empty">No data available</div>
          ) : (
            <div className="ent-table-wrap">
              <table className="ent-table">
                <thead>
                  <tr>
                    <th>Symbol</th>
                    <th>Size</th>
                    <th>Entry Price</th>
                    <th>PnL</th>
                  </tr>
                </thead>
                <tbody>
                  {d!.rows.map((p) => (
                    <tr key={p.symbol}>
                      <td>
                        <span className="ent-symbol-cell">
                          {p.symbol}
                          <span className={`ent-side-pill ${p.side.toLowerCase()}`}>{p.side}</span>
                        </span>
                      </td>
                      <td>{p.size}</td>
                      <td>{p.entryPrice}</td>
                      <td className={p.pnlPercent >= 0 ? "up" : "down"}>
                        {p.pnl >= 0 ? "+" : ""}
                        {p.pnl.toLocaleString()} ({p.pnlPercent >= 0 ? "+" : ""}
                        {p.pnlPercent.toFixed(2)}%)
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

          {res.stale && <div className="ent-stale-note">Showing cached values</div>}

          <div className="ent-panel-footer-actions">
            <button className="ent-btn" onClick={onViewAll} type="button">
              View All Positions
            </button>
            <button className="ent-btn primary" onClick={onNewOrder} type="button">
              <Plus size={14} /> New Order
            </button>
          </div>
        </>
      )}
    </Panel>
  );
}
