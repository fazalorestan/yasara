export type YasaraIndicatorReadiness = {
  indicator: "yasara";
  ready: boolean;
  score: number;
  v5PluginReady: boolean;
  executionAllowed: false;
  mode: "analysis_only";
};

export type YasaraIndicatorPipelineStage =
  | "pine_source_archive"
  | "settings_presets"
  | "runtime_adapter"
  | "chart_overlay_contract"
  | "engine_bridge"
  | "scanner_watchlist"
  | "alert_notification"
  | "readiness_gate";
