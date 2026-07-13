export interface PortfolioMetric { label: string; value: string; change?: string; tone?: "positive" | "negative" | "neutral"; }
export interface PositionRow { symbol: string; side: "LONG" | "SHORT"; entry: number; current: number; quantity: number; pnl: number; roe: number; tp: number; sl: number; }
export interface OrderRow { symbol: string; type: "LIMIT" | "MARKET" | "STOP"; side: "BUY" | "SELL"; price: number; quantity: number; status: "OPEN" | "FILLED" | "CANCELED"; }
export interface OrderBookRow { price: number; amount: number; total: number; }
export interface RecentTrade { time: string; price: number; amount: number; side: "buy" | "sell"; }

export const portfolioMetrics: PortfolioMetric[] = [
  { label: "Equity", value: "$10,245.80", change: "+2.45%", tone: "positive" },
  { label: "Available", value: "$8,920.00", change: "Safe mode", tone: "neutral" },
  { label: "Realized PnL", value: "$245.80", change: "+$245.80", tone: "positive" },
  { label: "Exposure", value: "12.9%", change: "Low risk", tone: "neutral" }
];

export const positions: PositionRow[] = [
  { symbol: "BTCUSDT", side: "LONG", entry: 49200, current: 50000, quantity: 0.01, pnl: 8, roe: 1.62, tp: 51500, sl: 48000 },
  { symbol: "ETHUSDT", side: "LONG", entry: 2920, current: 3000, quantity: 0.2, pnl: 16, roe: 2.73, tp: 3180, sl: 2840 },
  { symbol: "SOLUSDT", side: "SHORT", entry: 156, current: 150, quantity: 2, pnl: 12, roe: 3.84, tp: 142, sl: 161 }
];

export const orders: OrderRow[] = [
  { symbol: "BTCUSDT", type: "LIMIT", side: "BUY", price: 48500, quantity: 0.01, status: "OPEN" },
  { symbol: "ETHUSDT", type: "STOP", side: "SELL", price: 2840, quantity: 0.2, status: "OPEN" },
  { symbol: "SOLUSDT", type: "LIMIT", side: "SELL", price: 158, quantity: 1, status: "FILLED" }
];

export const asks: OrderBookRow[] = [
  { price: 50080, amount: 0.42, total: 21033 },
  { price: 50060, amount: 0.31, total: 15518 },
  { price: 50040, amount: 0.56, total: 28022 },
  { price: 50020, amount: 0.22, total: 11004 }
];

export const bids: OrderBookRow[] = [
  { price: 49980, amount: 0.35, total: 17493 },
  { price: 49960, amount: 0.49, total: 24480 },
  { price: 49940, amount: 0.27, total: 13483 },
  { price: 49920, amount: 0.61, total: 30451 }
];

export const recentTrades: RecentTrade[] = [
  { time: "12:01:08", price: 50012, amount: 0.012, side: "buy" },
  { time: "12:01:12", price: 50008, amount: 0.008, side: "sell" },
  { time: "12:01:17", price: 50020, amount: 0.031, side: "buy" },
  { time: "12:01:22", price: 50004, amount: 0.018, side: "sell" },
  { time: "12:01:30", price: 50028, amount: 0.011, side: "buy" }
];
