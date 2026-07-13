export interface WatchSymbol {
  symbol: string;
  exchange: string;
  price: number;
  change24h: number;
  volume: string;
  favorite?: boolean;
}

export const watchlist: WatchSymbol[] = [
  { symbol: "BTCUSDT", exchange: "binance", price: 50000, change24h: 2.4, volume: "1.2B", favorite: true },
  { symbol: "ETHUSDT", exchange: "binance", price: 3000, change24h: 1.8, volume: "620M", favorite: true },
  { symbol: "SOLUSDT", exchange: "toobit", price: 150, change24h: -0.9, volume: "210M" },
  { symbol: "XRPUSDT", exchange: "binance", price: 0.62, change24h: 3.1, volume: "180M" },
  { symbol: "BNBUSDT", exchange: "binance", price: 610, change24h: -1.2, volume: "155M" },
  { symbol: "ADAUSDT", exchange: "bitunix", price: 0.42, change24h: 0.7, volume: "94M" }
];

export const marketOverview = [
  { label: "Market Health", value: "Stable", hint: "4 active symbols" },
  { label: "Dominant Signal", value: "Neutral", hint: "AI regime average" },
  { label: "Risk Mode", value: "Safe", hint: "Live disabled" },
  { label: "Workspace", value: "Market", hint: "v1.2 Phase 2" }
];
