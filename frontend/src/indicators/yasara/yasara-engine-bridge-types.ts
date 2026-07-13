export type YasaraAIDecisionBridge = {
  source: "yasara_indicator";
  direction: "LONG" | "SHORT" | "WAIT";
  confidence: number;
  reason: string;
  mode: "analysis_only";
};

export type YasaraRiskBridge = {
  source: "yasara_indicator";
  riskLevel: "low" | "medium" | "neutral";
  executionAllowed: false;
  mode: "analysis_only";
};

export type YasaraScannerBridge = {
  symbol: string;
  indicator: "yasara";
  direction: "LONG" | "SHORT" | "WAIT";
  score: number;
  watchlistReady: boolean;
};

export type YasaraEngineBridgeOutput = {
  aiDecision: YasaraAIDecisionBridge;
  riskPanel: YasaraRiskBridge;
  scanner: YasaraScannerBridge;
  executionAllowed: false;
};
