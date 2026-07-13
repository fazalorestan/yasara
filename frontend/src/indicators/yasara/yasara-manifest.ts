export const yasaraIndicatorManifest = {
  name: "yasara",
  displayName: "YaSara",
  version: "v1.0",
  enabledByDefault: true,
  overlay: true,
  scriptSlot: "frontend/src/indicators/yasara/yasara-script.ts",
  updateStrategy: "replace-script-slot-only",
  capabilities: ["ema_overlay","smc_labels","fvg_zones","entry_sl_tp","dynamic_sl","relative_strength","confidence_score"],
} as const;
