import { ArrowRight } from "lucide-react";
import { Panel } from "./Panel";
import { useResilientResource } from "../hooks/useResilientResource";
import { getRiskEngineSummary } from "../api/riskEngine";
import { getBacktestResult } from "../api/riskBacktestPaper";
import "../styles/enterprise-panels.css";

interface RiskSnapshot {
  accountRiskLabel: string | null;
  accountRiskPercent: number | null;
  maxDrawdownPercent: number | null;
  varAmount: number | null;
  sharpeRatio: number | null;
  winRatePercent: number | null;
}

async function fetchRiskSnapshot(): Promise<RiskSnapshot | null> {
  const [riskRes, btRes] = await Promise.allSettled([getRiskEngineSummary(), getBacktestResult()]);
  const risk: any = riskRes.status === "fulfilled" ? riskRes.value : null;
  const bt: any = btRes.status === "fulfilled" ? btRes.value : null;

  // If neither source responded, this widget is genuinely unavailable.
  if (risk == null && bt == null) return null;

  return {
    accountRiskLabel: risk?.risk_level ?? risk?.level ?? null,
    accountRiskPercent: typeof risk?.exposure_percent === "number" ? risk.exposure_percent : null,
    maxDrawdownPercent: typeof bt?.max_drawdown_percent === "number" ? bt.max_drawdown_percent : null,
    varAmount: bt?.portfolio_var_95 ?? bt?.var_95 ?? null,
    sharpeRatio: typeof bt?.sharpe_ratio === "number" ? bt.sharpe_ratio : null,
    winRatePercent: bt?.win_rate_percent ?? bt?.win_rate ?? null,
  };
}

function riskBarTone(percent: number) {
  if (percent < 5) return "";
  if (percent < 15) return "tone-warning";
  return "tone-down";
}

/**
 * Risk Panel. Self-fetches from the existing risk-engine summary and
 * backtest endpoints via the shared resilient hook. Any field the
 * backend doesn't return shows "Unavailable" rather than a fabricated
 * number; the whole panel falls back to an Unavailable state if both
 * source endpoints fail.
 */
export function RiskPanel({ onOpenRiskManager }: { onOpenRiskManager?: () => void }) {
  const res = useResilientResource<RiskSnapshot>(fetchRiskSnapshot, { baseIntervalMs: 12000 });
  const d = res.data;

  return (
    <Panel title="Risk Panel">
      {!res.available ? (
        <div className="ent-empty">Unavailable</div>
      ) : (
        <>
          <div className="ent-risk-grid">
            <div className="ent-risk-stat">
              <span className="ent-risk-stat-label">Account Risk</span>
              <strong className="ent-risk-stat-value metric-tone-up">{d?.accountRiskLabel ?? "Unavailable"}</strong>
              {d?.accountRiskPercent != null && (
                <>
                  <span className="ent-risk-stat-value" style={{ fontSize: 12, fontWeight: 600 }}>
                    {d.accountRiskPercent.toFixed(2)}%
                  </span>
                  <div className="ent-risk-bar-track">
                    <div
                      className={`ent-risk-bar-fill ${riskBarTone(d.accountRiskPercent)}`}
                      style={{ width: `${Math.min(100, d.accountRiskPercent * 4)}%` }}
                    />
                  </div>
                </>
              )}
            </div>

            <div className="ent-risk-stat">
              <span className="ent-risk-stat-label">Max Drawdown</span>
              <strong className="ent-risk-stat-value metric-tone-down">
                {d?.maxDrawdownPercent != null ? `${d.maxDrawdownPercent.toFixed(2)}%` : "Unavailable"}
              </strong>
              {d?.maxDrawdownPercent != null && (
                <div className="ent-risk-bar-track">
                  <div
                    className={`ent-risk-bar-fill ${riskBarTone(d.maxDrawdownPercent)}`}
                    style={{ width: `${Math.min(100, d.maxDrawdownPercent * 4)}%` }}
                  />
                </div>
              )}
            </div>

            <div className="ent-risk-stat">
              <span className="ent-risk-stat-label">VaR (95%)</span>
              <strong className="ent-risk-stat-value">
                {d?.varAmount != null ? `$${Number(d.varAmount).toLocaleString()}` : "Unavailable"}
              </strong>
            </div>

            <div className="ent-risk-stat">
              <span className="ent-risk-stat-label">Sharpe Ratio</span>
              <strong className="ent-risk-stat-value">{d?.sharpeRatio != null ? d.sharpeRatio.toFixed(2) : "Unavailable"}</strong>
            </div>

            <div className="ent-risk-stat">
              <span className="ent-risk-stat-label">Win Rate</span>
              <strong className="ent-risk-stat-value">
                {d?.winRatePercent != null ? `${Number(d.winRatePercent).toFixed(1)}%` : "Unavailable"}
              </strong>
            </div>
          </div>

          {res.stale && <div className="ent-stale-note">Showing cached values</div>}

          <button
            className="ent-btn primary"
            style={{ width: "100%", justifyContent: "center", marginTop: 14 }}
            onClick={onOpenRiskManager}
            type="button"
          >
            Risk Manager <ArrowRight size={14} />
          </button>
        </>
      )}
    </Panel>
  );
}
