export interface MarketItem { exchange: string; symbol: string; normalized_symbol: string; last_price?: number; spread?: number; }
export interface MarketSnapshot { ready: boolean; count: number; items: MarketItem[]; }
export interface FinalReleaseSummary { ready: boolean; phase: string; progress_percent: number; safety: string; }
export interface AiDashboard { ready: boolean; count: number; items: Array<{ symbol: string; signal?: { direction?: string; score?: number; risk_level?: string }; regime?: { regime?: string; confidence?: number }; }>; }
