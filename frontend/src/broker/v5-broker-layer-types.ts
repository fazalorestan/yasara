export type YaSaraBrokerOrderRequest = { symbol: string; side: "buy" | "sell"; orderType: "market" | "limit"; quantity: number; price?: number | null; reduceOnly?: boolean; };
export type YaSaraBrokerOrderResult = { accepted: boolean; status: "blocked" | "accepted" | "rejected"; reason: string; executionAllowed: false; };
export type YaSaraBrokerSafetyPolicy = { liveExecutionAllowed: false; autoTradingAllowed: false; requiresLicense: boolean; requiresRiskApproval: boolean; };
