import { ChevronRight } from "lucide-react";
import { Panel } from "./Panel";
import { useResilientResource } from "../hooks/useResilientResource";
import { getAIFusionSummary } from "../api/aiFusion";
import "../styles/enterprise-panels.css";

interface AIFusionSnapshot {
  decision: string | null;
  confidencePercent: number | null;
  bias: string | null;
  strength: string | null;
  timeframe: string | null;
  strategy: string | null;
  riskLevel: string | null;
  recommendation: string | null;
  active: boolean;
}

async function fetchAIFusion(): Promise<AIFusionSnapshot | null> {
  const res: any = await getAIFusionSummary();
  if (res == null) return null;

  const confidence =
    typeof res.confidence === "number" ? (res.confidence <= 1 ? res.confidence * 100 : res.confidence) : null;

  return {
    decision: res.decision ?? res.call ?? null,
    confidencePercent: confidence,
    bias: res.bias ?? res.direction ?? null,
    strength: res.strength ?? null,
    timeframe: res.timeframe ?? null,
    strategy: res.strategy ?? null,
    riskLevel: res.risk_level ?? null,
    recommendation: res.recommendation ?? res.note ?? null,
    active: true,
  };
}

function toneFor(value: string | null): string {
  if (!value) return "";
  const v = value.toLowerCase();
  if (v === "bullish" || v === "long" || v === "low") return "metric-tone-up";
  if (v === "bearish" || v === "short" || v === "high") return "metric-tone-down";
  if (v === "medium") return "metric-tone-warning";
  return "";
}

/**
 * AI Decision Engine panel. Self-fetches from the existing ai-fusion
 * summary endpoint via the shared resilient hook. Individual fields the
 * backend doesn't return show "Unavailable" rather than a fabricated
 * value; the whole panel shows an Unavailable state if the endpoint
 * never responds.
 */
export function AIDecisionEngine({ onViewAnalysis }: { onViewAnalysis?: () => void }) {
  const res = useResilientResource<AIFusionSnapshot>(fetchAIFusion, { baseIntervalMs: 8000 });
  const d = res.data;

  const radius = 30;
  const circumference = 2 * Math.PI * radius;
  const clamped = Math.max(0, Math.min(100, d?.confidencePercent ?? 0));
  const offset = circumference - (clamped / 100) * circumference;

  return (
    <Panel
      title="AI Decision Engine"
      status={{ label: res.available ? "Active" : "Unavailable", tone: res.available ? "up" : "neutral" }}
    >
      {!res.available ? (
        <div className="ent-empty">Unavailable</div>
      ) : (
        <>
          <div className="ent-ai-decision-head">
            <svg width="72" height="72" viewBox="0 0 72 72">
              <circle cx="36" cy="36" r={radius} className="metric-ring-track" strokeWidth={6} fill="none" />
              {d?.confidencePercent != null && (
                <circle
                  cx="36"
                  cy="36"
                  r={radius}
                  className="metric-ring-value"
                  strokeWidth={6}
                  fill="none"
                  strokeDasharray={circumference}
                  strokeDashoffset={offset}
                  strokeLinecap="round"
                  transform="rotate(-90 36 36)"
                />
              )}
              <text x="36" y="33" textAnchor="middle" className="metric-ring-label" style={{ fontSize: 15, fontWeight: 800 }}>
                {d?.confidencePercent != null ? `${Math.round(clamped)}%` : "--"}
              </text>
              <text x="36" y="46" textAnchor="middle" style={{ fontSize: 7, fill: "var(--ent-text-dim)" }}>
                CONFIDENCE
              </text>
            </svg>
            <div>
              <div className="ent-ai-decision-value">{d?.decision ?? "Unavailable"}</div>
              <div className="ent-ai-decision-confidence">
                {d?.confidencePercent != null ? `Confidence ${Math.round(clamped)}%` : "Confidence unavailable"}
              </div>
            </div>
          </div>

          <div className="ent-ai-grid">
            <div className="ent-ai-grid-item">
              <span className="ent-ai-grid-label">Bias</span>
              <strong className={`ent-ai-grid-value ${toneFor(d?.bias ?? null)}`}>{d?.bias ?? "Unavailable"}</strong>
            </div>
            <div className="ent-ai-grid-item">
              <span className="ent-ai-grid-label">Strength</span>
              <strong className="ent-ai-grid-value">{d?.strength ?? "Unavailable"}</strong>
            </div>
            <div className="ent-ai-grid-item">
              <span className="ent-ai-grid-label">Timeframe</span>
              <strong className="ent-ai-grid-value">{d?.timeframe ?? "Unavailable"}</strong>
            </div>
            <div className="ent-ai-grid-item">
              <span className="ent-ai-grid-label">Strategy</span>
              <strong className="ent-ai-grid-value">{d?.strategy ?? "Unavailable"}</strong>
            </div>
            <div className="ent-ai-grid-item">
              <span className="ent-ai-grid-label">Risk Level</span>
              <strong className={`ent-ai-grid-value ${toneFor(d?.riskLevel ?? null)}`}>{d?.riskLevel ?? "Unavailable"}</strong>
            </div>
          </div>

          <div className="ent-ai-note">
            <strong style={{ display: "block", marginBottom: 4, color: "var(--ent-text)", fontSize: 11.5 }}>
              AI Recommendation
            </strong>
            {d?.recommendation ?? "No recommendation available."}
          </div>

          {res.stale && <div className="ent-stale-note">Showing cached values</div>}

          <button className="ent-link-action" onClick={onViewAnalysis} type="button">
            View Analysis <ChevronRight size={14} />
          </button>
        </>
      )}
    </Panel>
  );
}
