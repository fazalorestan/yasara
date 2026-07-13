export type YaSaraActivationStatus = "active" | "revoked" | "expired";

export type YaSaraDeviceActivation = {
  licenseKey: string;
  deviceFingerprint: string;
  activatedAt: string;
  status: YaSaraActivationStatus;
  executionAllowed: false;
};

export type YaSaraActivationPolicy = {
  offlineActivationSupported: true;
  deviceBindingSupported: true;
  executionAllowed: false;
};
