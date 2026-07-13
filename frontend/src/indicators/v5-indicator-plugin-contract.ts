export type V5IndicatorPluginContract = {
  name: string; version: string; displayName: string; overlay: boolean;
  enabledByDefault: boolean; capabilities: string[]; requiredContracts: string[];
  executionAllowed: false;
};
export type V5IndicatorCapabilityMatrixRow = {
  indicator: string; runtime: boolean; chartOverlay: boolean; scanner: boolean;
  alerts: boolean; settings: boolean; readiness: boolean;
};
