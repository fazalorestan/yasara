import { Search } from "lucide-react";
import { MetricCard, type MetricTone } from "./MetricCard";

export interface HeaderMetrics {
  totalEquity: string;
  equityTone: MetricTone;
  dailyPnl: string;
  dailyPnlTone: MetricTone;
  openPositions: string;
  openPositionsSub: string;
  riskLevel: string;
  riskTone: MetricTone;
  riskScoreLabel: string;
  aiConfidencePercent: number;
}

interface HeaderProps {
  workspaceTitle: string;
  workspaceSubtitle: string;
  metrics: HeaderMetrics;
  connected: boolean;
  loading: boolean;
  userInitials?: string;
  onSearch?: (value: string) => void;
}

export function Header({
  workspaceTitle,
  workspaceSubtitle,
  metrics,
  connected,
  loading,
  userInitials = "TP",
  onSearch,
}: HeaderProps) {
  return (
    <header className="ent-header">
      <div className="ent-header-title">
        <h1>
          {workspaceTitle}
          <span className="ent-header-caret">▾</span>
        </h1>
        <span>{workspaceSubtitle}</span>
      </div>

      <div className="ent-header-search">
        <Search size={16} />
        <input
          placeholder="Search symbol, strategy, order, or report..."
          onChange={(e) => onSearch?.(e.target.value)}
        />
      </div>

      <div className="ent-header-metrics">
        <MetricCard
          variant="chip"
          label="Total Equity"
          value={metrics.totalEquity}
          tone={metrics.equityTone}
          loading={loading}
        />
        <MetricCard
          variant="chip"
          label="Daily PnL"
          value={metrics.dailyPnl}
          tone={metrics.dailyPnlTone}
          loading={loading}
        />
        <MetricCard
          variant="chip"
          label="Open Positions"
          value={metrics.openPositions}
          sublabel={metrics.openPositionsSub}
          loading={loading}
        />
        <MetricCard
          variant="chip"
          label="Risk Level"
          value={metrics.riskLevel}
          sublabel={metrics.riskScoreLabel}
          tone={metrics.riskTone}
          loading={loading}
        />
        <MetricCard
          variant="chip"
          label="AI Confidence"
          value={`${Math.round(metrics.aiConfidencePercent)}%`}
          ringPercent={metrics.aiConfidencePercent}
          loading={loading}
        />
      </div>

      <div className="ent-header-status">
        <span className={`ent-conn-dot ${connected ? "ok" : "down"}`} />
        <button className="ent-avatar" title="Account">
          {userInitials}
        </button>
      </div>
    </header>
  );
}
