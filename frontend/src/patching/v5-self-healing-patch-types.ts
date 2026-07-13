export type YaSaraSelfHealingPatchSummary = { ready: boolean; autoDiscoveryEnabled: boolean; dryRunSupported: boolean; manifestSupported: boolean; };
export type YaSaraPatchDryRunPlan = { ready: boolean; totalScripts: number; dryRun: boolean; };
export type YaSaraPatchManifest = { ready: boolean; lastPatch: string | null; installed: string[]; failed: string[]; };
