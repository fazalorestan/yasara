export type YaSaraExchangeType = "crypto" | "forex" | "stock" | "commodity" | "index" | "iran_market" | "custom";

export type YaSaraExchangeInfo = {
  exchangeId: string;
  name: string;
  exchangeType: YaSaraExchangeType;
  region: "global" | "iran" | string;
  enabled: boolean;
};

export type YaSaraExchangeCapability = {
  spot: boolean;
  futures: boolean;
  margin: boolean;
  options: boolean;
  rest: boolean;
  websocket: boolean;
  orderbook: boolean;
  trades: boolean;
  ohlcv: boolean;
  ticker: boolean;
  sandbox: boolean;
  testnet: boolean;
  iranMarket: boolean;
};

export type YaSaraExchangeHealth = {
  exchangeId: string;
  status: "connected" | "disconnected" | "maintenance" | "rate_limited";
  latencyMs: number | null;
  reconnectCount: number;
  maintenance: boolean;
  rateLimited: boolean;
};
