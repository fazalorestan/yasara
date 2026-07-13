export type YasaraIndicatorHandoff = {
  indicator: "yasara";
  version: "v1.0";
  status: "ready_for_v5";
  executionAllowed: false;
  mode: "analysis_only";
};

export type YasaraV5IndicatorPluginContract = {
  pluginType: "indicator";
  requiredFiles: string[];
  forbidden: string[];
  communication: string[];
};
