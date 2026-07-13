import { Panel } from "./Panel";
import { useResilientPoll } from "../hooks/useResilientPoll";
import { getBacktestResult } from "../api/riskBacktestPaper";

interface RiskAnalysisData {
  portfolioVar95: string;
  maxDrawdownPercent: number;
  sharpeRatio: number;
  winRatePercent: number;
}

const dim = "var(--ent-text-dim, #8b93a7)";
const up = "var(--ent-up, #22c55e)";
const down = "var(--ent-down, #ef4444)";

async function fetchRiskAnalysis(): Promise<RiskAnalysisData> {
  const res: any = await getBacktestResult();
  const varValue = res?.portfolio_var_95 ?? res?.var_95;
  const drawdown = res?.max_drawdown_percent;
  const sharpe = res?.sharpe_ratio;
  const winRate = res?.win_rate_percent ?? res?.win_rate;

  if (varValue == null || drawdown == null || sharpe == null || winRate == null) {
    throw new Error("risk analysis unavailable");
  }

  return {
    portfolioVar95: `$${Number(varValue).toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`,
    maxDrawdownPercent: drawdown,
    sharpeRatio: sharpe,
    winRatePercent: winRate,
  };
}

function Stat({ label, value, valueColor }: { label: string; value: string; valueColor?: string }) {
  return (
    <div style={{ padding: "10px 12px", borderRadius: 8, background: "rgba(255,255,255,0.03)" }}>
      <div style={{ fontSize: 10.5, letterSpacing: "0.06em", textTransform: "uppercase", color: dim }}>{label}</div>
      <strong style={{ fontSize: 17, color: valueColor ?? "inherit", display: "block", marginTop: 4 }}>{value}</strong>
    </div>
  );
}

export function RiskAnalysis() {
  const poll = useResilientPoll<RiskAnalysisData>(fetchRiskAnalysis, { baseIntervalMs: 12000 });

  return (
    <Panel title="Risk Analysis">
      {!poll.available ? (
        <div style={{ fontSize: 12, color: dim, padding: "18px 0", textAlign: "center" }}>Unavailable</div>
      ) : (
        <>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10 }}>
            <Stat label="Portfolio VaR (95%)" value={poll.data!.portfolioVar95} />
            <Stat label="Max Drawdown" value={`${poll.data!.maxDrawdownPercent}%`} valueColor={down} />
            <Stat label="Sharpe Ratio" value={poll.data!.sharpeRatio.toFixed(2)} />
            <Stat label="Win Rate" value={`${poll.data!.winRatePercent}%`} valueColor={up} />
          </div>
          {poll.stale && <div style={{ fontSize: 10, color: dim, marginTop: 8 }}>Showing cached values</div>}
        </>
      )}
    </Panel>
  );
}
