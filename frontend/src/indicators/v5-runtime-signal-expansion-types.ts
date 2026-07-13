export type V5SignalScoreBand = "very_strong" | "strong" | "moderate" | "weak" | "no_trade";

export type V5ExpandedRuntimeSignal = {
  indicator: "yasara";
  direction: "LONG" | "SHORT" | "WAIT";
  confidence: number;
  band: V5SignalScoreBand;
  reasons: string[];
  reasonCodes: string[];
  executionAllowed: false;
  mode: "analysis_only";
};
