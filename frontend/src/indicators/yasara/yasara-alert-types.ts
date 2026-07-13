export type YasaraAlertSeverity = "critical" | "warning" | "info" | "silent";

export type YasaraIndicatorAlert = {
  id: string;
  indicator: "yasara";
  symbol: string;
  direction: "LONG" | "SHORT" | "WAIT";
  confidence: number;
  severity: YasaraAlertSeverity;
  message: string;
  executionAllowed: false;
};

export type YasaraIndicatorNotificationEvent = {
  name: "IndicatorNotificationRequested";
  source: "yasara_indicator";
  alert: YasaraIndicatorAlert;
  mode: "analysis_only";
};
