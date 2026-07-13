export type YaSaraRiskPolicy = { maxRiskPerTradePct: number; maxDailyLossPct: number; maxDrawdownPct: number; liveExecutionAllowed: false; autoTradingAllowed: false; };
export type YaSaraPositionSizeResult = { ready: boolean; riskAmount: number; stopDistance: number; quantity: number; };
export type YaSaraRiskPreflight = { ready: boolean; allowed: boolean; reason: string; executionAllowed: false; };
