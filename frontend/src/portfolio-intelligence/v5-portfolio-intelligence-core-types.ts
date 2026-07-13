export type YaSaraPortfolioAsset = { symbol: string; value: number; targetWeight: number; currentWeight?: number; };
export type YaSaraPortfolioAllocation = { ready: boolean; totalValue: number; assets: YaSaraPortfolioAsset[]; };
export type YaSaraPortfolioRebalanceAction = { symbol: string; drift: number; action: "buy" | "sell" | "hold"; };
