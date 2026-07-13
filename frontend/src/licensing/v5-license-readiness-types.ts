export type YaSaraLicenseReadinessGate = {
  ready: boolean;
  score: number;
  subsystem: "license_entitlement";
  executionAllowed: false;
};

export type YaSaraLicenseCompatibility = {
  v5Compatible: boolean;
  offlineMode: boolean;
  onlineFutureReady: boolean;
  pluginReady: boolean;
  demoSupported: boolean;
};
