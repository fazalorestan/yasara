import { Panel } from "./Panel";
import { useResilientResource } from "../hooks/useResilientResource";
import { getOperationalMarketSnapshot } from "../api/realData";
import "../styles/enterprise-panels.css";

interface RawSnapshot {
  total_market_cap?: number;
  btc_dominance?: number;
  volume_24h?: number;
  fear_greed?: number;
  high_24h?: number;
  low_24h?: number;
  change_24h_percent?: number;
  market_trend?: string;
  altcoin_season_index?: number;
}

function currency(v: number | undefined): string {
  return typeof v === "number" ? `$${v.toLocaleString(undefined, { maximumFractionDigits: 2 })}` : "Unavailable";
}
function percent(v: number | undefined): string {
  return typeof v === "number" ? `${v.toFixed(2)}%` : "Unavailable";
}

/**
 * Market Overview panel. Self-fetches from the existing
 * /v2-1/real-data/market-snapshot endpoint via the shared resilient hook.
 * No mock data: any field the backend doesn't return renders "Unavailable"
 * instead of a fabricated number; the whole panel shows an Unavailable
 * state if the endpoint never responds.
 */
export function MarketOverview({ onViewAll }: { onViewAll?: () => void }) {
  const res = useResilientResource<RawSnapshot>(() => getOperationalMarketSnapshot("all"), { baseIntervalMs: 10000 });
  const d = res.data;

  return (
    <Panel title="Market Overview" action={<span onClick={onViewAll} style={{ cursor: "pointer" }}>View All</span>}>
      {!res.available ? (
        <div className="ent-empty">Unavailable</div>
      ) : (
        <>
          <div className="ent-overview-grid">
            <div className="ent-overview-item">
              <span>24H High</span>
              <strong>{currency(d?.high_24h)}</strong>
            </div>
            <div className="ent-overview-item">
              <span>24H Low</span>
              <strong className={d?.low_24h != null ? "metric-tone-down" : undefined}>{currency(d?.low_24h)}</strong>
            </div>
            <div className="ent-overview-item">
              <span>24H Volume</span>
              <strong>{currency(d?.volume_24h)}</strong>
            </div>
            <div className="ent-overview-item">
              <span>24H Change</span>
              <strong className={(d?.change_24h_percent ?? 0) >= 0 ? "metric-tone-up" : "metric-tone-down"}>
                {typeof d?.change_24h_percent === "number"
                  ? `${d.change_24h_percent >= 0 ? "+" : ""}${d.change_24h_percent.toFixed(2)}%`
                  : "Unavailable"}
              </strong>
            </div>
            <div className="ent-overview-item">
              <span>Market Cap</span>
              <strong>{currency(d?.total_market_cap)}</strong>
            </div>
            <div className="ent-overview-item">
              <span>Dominance</span>
              <strong>{percent(d?.btc_dominance)}</strong>
            </div>
            <div className="ent-overview-item">
              <span>Fear &amp; Greed</span>
              <strong className="metric-tone-up">{typeof d?.fear_greed === "number" ? d.fear_greed : "Unavailable"}</strong>
            </div>
            <div className="ent-overview-item">
              <span>Market Trend</span>
              <strong className="metric-tone-up">{d?.market_trend ?? "Unavailable"}</strong>
            </div>
            <div className="ent-overview-item">
              <span>Altcoin Season</span>
              <strong>{typeof d?.altcoin_season_index === "number" ? `${d.altcoin_season_index}/100` : "Unavailable"}</strong>
            </div>
          </div>
          {res.stale && <div className="ent-stale-note">Showing cached values</div>}
        </>
      )}
    </Panel>
  );
}
