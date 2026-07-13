export type YaSaraMarketSymbol = {
  symbol: string;
  baseAsset: string;
  quoteAsset: string;
  marketType: "crypto" | "forex" | "iran_market" | string;
  exchange: string;
  enabled: boolean;
};

export type YaSaraOHLCV = {
  symbol: string;
  timeframe: string;
  openTime: number;
  open: number;
  high: number;
  low: number;
  close: number;
  volume: number;
  exchange: string;
};

export type YaSaraOrderBookLevel = {
  price: number;
  quantity: number;
};

export type YaSaraMarketSnapshot = {
  symbol: string;
  lastPrice: number;
  change24h: number;
  volume24h: number;
  exchange: string;
};
