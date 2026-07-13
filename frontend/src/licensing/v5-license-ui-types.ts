export type YaSaraLicenseStatusCard = {
  title: "License Status";
  licenseType: string;
  featuresCount: number;
  expired: boolean;
  validTime: boolean;
  badge: string;
  executionAllowed: false;
};

export type YaSaraFeatureLockState = {
  feature: string;
  locked: boolean;
  reason: string;
};

export type YaSaraLicenseSettingsContract = {
  sections: string[];
  actions: string[];
  executionAllowed: false;
};
