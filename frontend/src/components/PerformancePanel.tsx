import { useState } from "react";
import { Panel } from "./Panel";
import { useResilientResource } from "../hooks/useResilientResource";
import { getBacktestResult, getPaperState } from "../api/riskBacktestPaper";
import "../styles/enterprise-panels.css";

export type PerformanceRange = "1D" | "7D" | "1M" | "3M" | "1Y" | "ALL";
const RANGES: PerformanceRange[] = ["1D", "7D", "1M", "3M", "1Y", "ALL"];

interface PerformanceStat {
  label: string;
  value: string;
}

interface PerformanceSnapshot {
  totalReturnPercent: number;
  series: number[];
  stats: PerformanceStat[];
}

async function fetchPerformance(): Promise<PerformanceSnapshot | null> {
  const [paperRes, btRes] = await Promise.allSettled([getPaperState(), getBacktestResult()]);
  const paper: any = paperRes.status === "fulfilled" ? paperRes.value : null;
  const bt: any = btRes.status === "fulfilled" ? btRes.value : null;

  const totalReturnPercent = paper?.total_return_percent ?? bt?.total_return_percent;
  const series = paper?.equity_curve ?? bt?.equity_curve;

  if (typeof totalReturnPercent !== "number" || !Array.isArray(series) || series.length < 2) return null;

  const varValue = bt?.portfolio_var_95 ?? bt?.var_95;
  const drawdown = bt?.max_drawdown_percent;
  const sharpe = bt?.sharpe_ratio;
  const winRate = bt?.win_rate_percent ?? bt?.win_rate;

  const stats: PerformanceStat[] = [
    { label: "Portfolio VaR (95%)", value: varValue != null ? `$${Number(varValue).toLocaleString()}` : "Unavailable" },
    { label: "Max Drawdown", value: typeof drawdown === "number" ? `${drawdown.toFixed(2)}%` : "Unavailable" },
    { label: "Sharpe Ratio", value: typeof sharpe === "number" ? sharpe.toFixed(2) : "Unavailable" },
    { label: "Win Rate", value: winRate != null ? `${Number(winRate).toFixed(1)}%` : "Unavailable" },
  ];

  return { totalReturnPercent, series, stats };
}

function buildPath(series: number[], width: number, height: number) {
  const max = Math.max(...series);
  const min = Math.min(...series);
  const range = max - min || 1;
  const step = width / (series.length - 1);
  return series
    .map((v, i) => {
      const x = i * step;
      const y = height - ((v - min) / range) * height;
      return `${i === 0 ? "M" : "L"}${x.toFixed(1)},${y.toFixed(1)}`;
    })
    .join(" ");
}

/**
 * Performance panel. Self-fetches from the existing paper-state and
 * backtest endpoints via the shared resilient hook. Shows "Unavailable"
 * with no chart and no fabricated stats if neither source responds.
 */
export function PerformancePanel() {
  const [range, setRange] = useState<PerformanceRange>("1M");
  const res = useResilientResource<PerformanceSnapshot>(fetchPerformance, { baseIntervalMs: 12000 });
  const d = res.data;

  const width = 260;
  const height = 70;
  const positive = (d?.totalReturnPercent ?? 0) >= 0;

  return (
    <Panel title="Performance">
      <div className="ent-tabbar">
        {RANGES.map((r) => (
          <button key={r} className={range === r ? "active" : ""} onClick={() => setRange(r)} type="button">
            {r}
          </button>
        ))}
      </div>

      {!res.available ? (
        <div className="ent-empty">Unavailable</div>
      ) : (
        <>
          <div className="ent-perf-head">
            <div>
              <div className="ent-perf-sub">Total Return</div>
              <strong className={`ent-perf-return ${positive ? "metric-tone-up" : "metric-tone-down"}`}>
                {positive ? "+" : ""}
                {d!.totalReturnPercent.toFixed(2)}%
              </strong>
            </div>
          </div>

          <svg viewBox={`0 0 ${width} ${height}`} className="ent-perf-chart" preserveAspectRatio="none">
            <defs>
              <linearGradient id="ent-perf-fill" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stopColor="var(--ent-up)" stopOpacity="0.35" />
                <stop offset="100%" stopColor="var(--ent-up)" stopOpacity="0" />
              </linearGradient>
            </defs>
            <path d={`${buildPath(d!.series, width, height)} L${width},${height} L0,${height} Z`} fill="url(#ent-perf-fill)" stroke="none" />
            <path d={buildPath(d!.series, width, height)} fill="none" stroke="var(--ent-up)" strokeWidth={2} />
          </svg>

          <div className="ent-perf-stats">
            {d!.stats.map((s) => (
              <div className="ent-perf-stat" key={s.label}>
                <span className="ent-perf-stat-label">{s.label}</span>
                <span className="ent-perf-stat-value">{s.value}</span>
              </div>
            ))}
          </div>

          {res.stale && <div className="ent-stale-note">Showing cached values</div>}
        </>
      )}
    </Panel>
  );
}
