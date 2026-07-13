export type V5IndicatorSandboxPolicy = {
  allowNetwork: false;
  allowFileWrite: false;
  allowLiveExecution: false;
  allowExchangeOrders: false;
  mode: "sandbox_contract_only";
};

export type V5IndicatorValidationResult = {
  valid: boolean;
  errors: string[];
  warnings: string[];
};

export type V5IndicatorInstallGate = {
  ready: boolean;
  installAllowed: boolean;
  executionAllowed: false;
};
