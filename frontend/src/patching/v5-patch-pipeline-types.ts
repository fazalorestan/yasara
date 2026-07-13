export type YaSaraPatchScriptClassification = { script: string; family: "v5" | "v4" | "v3" | "legacy"; isRouterPatch: boolean; safe: boolean; };
export type YaSaraPatchPipelinePlan = { ready: boolean; totalScripts: number; safeScripts: number; v5Scripts: number; v5AutoDiscoveryEnabled: boolean; };
