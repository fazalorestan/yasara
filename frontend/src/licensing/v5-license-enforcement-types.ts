export type YaSaraFeatureGateResult = {
  feature: string;
  allowed: boolean;
  reason: string;
  executionAllowed: false;
};

export type YaSaraDemoLimits = {
  alertLimit: number;
  indicatorLimit: number;
  workspaceLimit: number;
  exportAllowed: false;
  apiAccessAllowed: false;
  autoTradingAllowed: false;
};

export type YaSaraLicenseFlags = Record<string, boolean>;
