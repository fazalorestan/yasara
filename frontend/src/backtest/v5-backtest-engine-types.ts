export type YaSaraBacktestConfig = { strategyId: string; symbol: string; timeframe: string; initialEquity: number; feePct: number; slippagePct: number; riskPct: number; };
export type YaSaraSimulatedTrade = { symbol: string; side: "long" | "short"; entryPrice: number; exitPrice: number; quantity: number; pnl: number; };
export type YaSaraBacktestReport = { ready: boolean; totalTrades: number; netPnl: number; winRate: number; maxDrawdownPct: number; };
