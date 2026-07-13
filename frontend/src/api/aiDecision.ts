export interface EvidenceItem {
  source: string;
  status: "confirmed" | "rejected" | "unavailable";
  score?: number | null;
  reason?: string | null;
  payload?: Record<string, unknown>;
}
export interface FusionRequest {
  symbol: string;
  timeframe: string;
  evidences: EvidenceItem[];
  risk_score?: number | null;
  portfolio_exposure?: number | null;
}
export async function requestAIDecision(payload: FusionRequest) {
  const r = await fetch("/api/v1/ai/decision", {
    method: "POST",
    headers: {"Content-Type":"application/json","Accept":"application/json"},
    body: JSON.stringify(payload),
  });
  if (!r.ok) throw new Error(`AI decision failed: ${r.status}`);
  return r.json();
}
export async function getAITimeline(limit=100) {
  const r = await fetch(`/api/v1/ai/timeline?limit=${limit}`);
  if (!r.ok) throw new Error(`AI timeline failed: ${r.status}`);
  return r.json();
}
