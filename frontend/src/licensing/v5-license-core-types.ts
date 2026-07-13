export type YaSaraLicenseType = "demo" | "personal" | "pro" | "elite" | "enterprise" | "lifetime" | "internal";

export type YaSaraFeature =
  | "DASHBOARD"
  | "BASIC_ANALYSIS"
  | "ADVANCED_AI"
  | "SCANNER"
  | "ALERTS"
  | "JOURNAL"
  | "BACKTEST"
  | "STRATEGY_BUILDER"
  | "FOREX"
  | "IRAN_MARKET"
  | "MARKETPLACE"
  | "EXPORT"
  | "API_ACCESS"
  | "AUTO_TRADING"
  | "AI_COACH"
  | "ENTERPRISE_DASHBOARD"
  | "TELEGRAM_COACH";

export type YaSaraLicenseEntitlement = {
  licenseType: YaSaraLicenseType;
  features: Partial<Record<YaSaraFeature, boolean>>;
  executionAllowed: false;
};
