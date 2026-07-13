export type YaSaraScannerWatchlist = { name: string; symbols: string[]; marketType: string; enabled: boolean; };
export type YaSaraScanCriteria = { minScore: number; maxRiskPct: number; requireTrendAlignment: boolean; requireVolumeConfirmation: boolean; };
export type YaSaraSignalCandidate = { symbol: string; direction: "long" | "short"; score: number; riskPct: number; reason: string; };
export type YaSaraScannerResult = { ready: boolean; total: number; accepted: number; rejected: number; executionAllowed: false; };
