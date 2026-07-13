export type MetricTone = "up" | "down" | "neutral" | "warning" | "danger";

export interface MetricCardProps {
  label: string;
  value: string;
  sublabel?: string;
  tone?: MetricTone;
  variant?: "chip" | "panel";
  ringPercent?: number;
  loading?: boolean;
}

function toneClass(tone: MetricTone = "neutral") {
  return `metric-tone-${tone}`;
}

function ConfidenceRing({ percent }: { percent: number }) {
  const clamped = Math.max(0, Math.min(100, percent));
  const radius = 16;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (clamped / 100) * circumference;
  return (
    <svg width="40" height="40" viewBox="0 0 40 40" className="metric-ring">
      <circle cx="20" cy="20" r={radius} className="metric-ring-track" />
      <circle
        cx="20"
        cy="20"
        r={radius}
        className="metric-ring-value"
        strokeDasharray={circumference}
        strokeDashoffset={offset}
      />
      <text x="20" y="23" textAnchor="middle" className="metric-ring-label">
        {Math.round(clamped)}
      </text>
    </svg>
  );
}

export function MetricCard({
  label,
  value,
  sublabel,
  tone = "neutral",
  variant = "panel",
  ringPercent,
  loading,
}: MetricCardProps) {
  return (
    <div className={`metric-card metric-${variant} ${toneClass(tone)} ${loading ? "metric-loading" : ""}`}>
      {typeof ringPercent === "number" && <ConfidenceRing percent={ringPercent} />}
      <div className="metric-body">
        <span className="metric-label">{label}</span>
        <strong className="metric-value">{loading ? "—" : value}</strong>
        {sublabel && <small className="metric-sublabel">{sublabel}</small>}
      </div>
    </div>
  );
}
