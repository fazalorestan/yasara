import { apiGet } from "./client";
export const getMarketEngineTick = (symbol = "BTCUSDT", exchange = "binance") => apiGet(`/v2-2/market-engine/tick?symbol=${symbol}&exchange=${exchange}`);
export const getMarketEngineOhlc = (symbol = "BTCUSDT", exchange = "binance", timeframe = "4H", limit = 120) => apiGet(`/v2-2/market-engine/ohlc?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}&limit=${limit}`);
export const getMarketEngineSnapshot = (exchange = "all") => apiGet(`/v2-2/market-engine/snapshot?exchange=${exchange}`);
