export const yasaraUpdateContract = {
  indicator: "yasara",
  editableFile: "frontend/src/indicators/yasara/yasara-script.ts",
  stableContracts: [
    "frontend/src/indicators/indicator-registry.ts",
    "frontend/src/indicators/chart-indicator-manager.ts",
    "frontend/src/indicators/yasara/yasara-renderer-contract.ts",
  ],
  rule: "Update indicator logic by replacing yasara-script.ts only.",
  backwardCompatible: true,
} as const;
