import { Panel } from "./Panel";
import { useResilientResource } from "../hooks/useResilientResource";
import { getNotificationAlertsSummary } from "../api/notificationAlerts";
import "../styles/enterprise-panels.css";

export interface NewsItem {
  id: string;
  timeAgo: string;
  headline: string;
  tag: string;
}

function timeAgo(iso: string): string {
  const then = new Date(iso).getTime();
  if (Number.isNaN(then)) return iso;
  const diffMin = Math.max(0, Math.round((Date.now() - then) / 60000));
  if (diffMin < 1) return "just now";
  if (diffMin < 60) return `${diffMin}m ago`;
  return `${Math.round(diffMin / 60)}h ago`;
}

async function fetchNews(): Promise<NewsItem[] | null> {
  const res: any = await getNotificationAlertsSummary();
  const list = res?.events ?? res?.recent;
  if (!Array.isArray(list)) return null;
  return list.map((e: any, i: number) => ({
    id: String(e.id ?? i),
    timeAgo: e.timestamp ? timeAgo(e.timestamp) : e.time ?? "--",
    headline: e.headline ?? e.message ?? e.title ?? "Event",
    tag: e.category ?? e.tag ?? "Market",
  }));
}

/**
 * News & Events panel. Self-fetches from the existing notifications
 * summary endpoint via the shared resilient hook. Shows "Unavailable"
 * if the endpoint never responds, and "No data available" if it
 * responds with zero items - never fabricated headlines.
 */
export function NewsEvents({ onViewAll }: { onViewAll?: () => void }) {
  const res = useResilientResource<NewsItem[]>(fetchNews, { baseIntervalMs: 15000 });

  return (
    <Panel title="News &amp; Events" action={<span onClick={onViewAll} style={{ cursor: "pointer" }}>View All</span>}>
      {!res.available ? (
        <div className="ent-empty">Unavailable</div>
      ) : res.data!.length === 0 ? (
        <div className="ent-empty">No data available</div>
      ) : (
        <>
          {res.data!.map((item) => (
            <div className="ent-news-item" key={item.id}>
              <div className="ent-news-meta">
                <span className="ent-news-time">{item.timeAgo}</span>
                <span className="ent-tag">{item.tag}</span>
              </div>
              <div className="ent-news-headline">{item.headline}</div>
            </div>
          ))}
          {res.stale && <div className="ent-stale-note">Showing cached values</div>}
        </>
      )}
    </Panel>
  );
}
