export type V5RuntimeSignalDirection = "LONG" | "SHORT" | "WAIT";

export type V5RuntimeSignalLogicOutput = {
  indicator: "yasara";
  direction: V5RuntimeSignalDirection;
  confidence: number;
  reasons: string[];
  executionAllowed: false;
  mode: "analysis_only";
};
