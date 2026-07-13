import { useState } from "react";
import { Plus } from "lucide-react";
import { Panel } from "./Panel";
import { useResilientResource } from "../hooks/useResilientResource";
import { getPaperState } from "../api/riskBacktestPaper";
import "../styles/enterprise-panels.css";

export interface OpenOrderRow {
  symbol: string;
  side: "BUY" | "SELL";
  type: string;
  size: string;
  price: string;
  status: string;
}

async function fetchOrders(): Promise<OpenOrderRow[] | null> {
  const res: any = await getPaperState();
  const list = res?.orders;
  if (!Array.isArray(list)) return null;
  return list.map((o: any) => ({
    symbol: o.symbol ?? "--",
    side: (o.side ?? "BUY").toUpperCase(),
    type: o.type ?? o.order_type ?? "LIMIT",
    size: o.qty != null ? String(o.qty) : "--",
    price: o.price != null ? Number(o.price).toLocaleString() : "--",
    status: o.status ?? "OPEN",
  }));
}

/**
 * Orders panel. Self-fetches from the existing paper-trading state
 * endpoint via the shared resilient hook. Shows "Unavailable" if the
 * endpoint never responds, and "No data available" per tab if it
 * responds with zero matching orders - never fabricated rows.
 */
export function OrdersPanel({ onNewOrder }: { onNewOrder?: () => void }) {
  const [tab, setTab] = useState<"open" | "history">("open");
  const res = useResilientResource<OpenOrderRow[]>(fetchOrders, { baseIntervalMs: 6000 });

  const rows = (res.data ?? []).filter((r) => (tab === "open" ? r.status.toUpperCase() === "OPEN" : r.status.toUpperCase() !== "OPEN"));

  return (
    <Panel title="Orders">
      <div className="ent-tabbar">
        <button className={tab === "open" ? "active" : ""} onClick={() => setTab("open")} type="button">
          Open
        </button>
        <button className={tab === "history" ? "active" : ""} onClick={() => setTab("history")} type="button">
          History
        </button>
      </div>

      {!res.available ? (
        <div className="ent-empty">Unavailable</div>
      ) : rows.length === 0 ? (
        <div className="ent-empty">No data available</div>
      ) : (
        <div className="ent-table-wrap">
          <table className="ent-table">
            <thead>
              <tr>
                <th>Symbol</th>
                <th>Type</th>
                <th>Size</th>
                <th>Price</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((o, i) => (
                <tr key={`${o.symbol}-${i}`}>
                  <td>
                    <span className="ent-symbol-cell">
                      {o.symbol}
                      <span className={`ent-side-pill ${o.side.toLowerCase()}`}>{o.side}</span>
                    </span>
                  </td>
                  <td>{o.type}</td>
                  <td>{o.size}</td>
                  <td>{o.price}</td>
                  <td>
                    <span className="ent-status-pill open">{o.status}</span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {res.stale && <div className="ent-stale-note">Showing cached values</div>}

      <div className="ent-panel-footer-actions">
        <button className="ent-btn primary" style={{ width: "100%", justifyContent: "center" }} onClick={onNewOrder} type="button">
          <Plus size={14} /> New Order
        </button>
      </div>
    </Panel>
  );
}
