import { Panel } from "./Panel";
import { useResilientResource } from "../hooks/useResilientResource";
import { getAlertHistory } from "../api/notificationAlerts";
import "../styles/enterprise-panels.css";

export interface AlertItem {
  id: string;
  timeAgo: string;
  symbol: string;
  detail: string;
  status: "trigger" | "active";
}

async function fetchAlerts(): Promise<AlertItem[] | null> {
  const res: any = await getAlertHistory();
  const list = res?.alerts;
  if (!Array.isArray(list)) return null;
  return list.map((a: any, i: number) => ({
    id: String(a.id ?? i),
    timeAgo: a.time ?? a.timestamp ?? "--",
    symbol: a.symbol ?? a.title ?? a.type ?? "Alert",
    detail: a.detail ?? a.message ?? "",
    status: a.severity === "high" || a.severity === "medium" ? "trigger" : "active",
  }));
}

/**
 * Alerts panel. Self-fetches from the existing notifications/alerts
 * endpoint via the shared resilient hook. Renders "Unavailable" if the
 * endpoint never responds, and "No data available" if it responds with
 * zero alerts - never fabricated alert rows.
 */
export function AlertsPanel({ onViewAll }: { onViewAll?: () => void }) {
  const res = useResilientResource<AlertItem[]>(fetchAlerts, { baseIntervalMs: 8000 });

  return (
    <Panel title="Alerts" action={<span onClick={onViewAll} style={{ cursor: "pointer" }}>View All</span>}>
      {!res.available ? (
        <div className="ent-empty">Unavailable</div>
      ) : res.data!.length === 0 ? (
        <div className="ent-empty">No data available</div>
      ) : (
        <>
          {res.data!.map((a) => (
            <div className="ent-row" key={a.id}>
              <div className="ent-row-main">
                <span className="ent-row-sub">{a.timeAgo}</span>
                <span className="ent-row-title">{a.symbol}</span>
                <span className="ent-row-sub">{a.detail}</span>
              </div>
              <span className={a.status === "trigger" ? "ent-status-pill open" : "ent-status-pill"}>
                {a.status === "trigger" ? "Trigger" : "Active"}
              </span>
            </div>
          ))}
          {res.stale && <div className="ent-stale-note">Showing cached values</div>}
        </>
      )}
    </Panel>
  );
}
