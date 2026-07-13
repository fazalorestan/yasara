export type YaSaraPortfolioHolding = { symbol: string; quantity: number; averagePrice: number; lastPrice: number; assetClass: string; };
export type YaSaraPortfolioSnapshot = { accountId: string; totalEquity: number; cashBalance: number; holdingsValue: number; unrealizedPnl: number; };
export type YaSaraAllocationItem = { symbol: string; value: number; weightPct: number; };
export type YaSaraPortfolioRiskCheck = { ready: boolean; allowed: boolean; reason: string; executionAllowed: false; };
