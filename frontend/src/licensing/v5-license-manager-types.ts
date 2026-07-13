export type YaSaraLicenseManagerStatus = {
  licenseType: string;
  featuresCount: number;
  expired: boolean;
  validTime: boolean;
  executionAllowed: false;
};

export type YaSaraLicensePlan = {
  licenseType: string;
  duration: number | "lifetime";
  features: string[];
  deviceLimit: number;
  executionAllowed: false;
};

export type YaSaraAdminLicenseOperation =
  | "create_license"
  | "renew_license"
  | "revoke_license"
  | "inspect_license"
  | "export_license"
  | "import_license"
  | "assign_features"
  | "change_device_limit";
