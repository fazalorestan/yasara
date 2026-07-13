export type V5IndicatorReleaseGate = {
  ready: boolean;
  milestone: "1000_tests";
  score: number;
  executionAllowed: false;
};

export type V5IndicatorAlphaStability = {
  alpha: "v5.0-alpha.5";
  stability: "green" | "yellow" | "red";
  regressionRisk: "low" | "medium" | "high";
  safeToContinue: boolean;
};
