import { apiGet } from "./client";

export const getLiveExchangeSummary = () =>
  apiGet("/v3-1/live-exchange/summary");

export const getLiveTick = (symbol = "BTCUSDT", exchange = "binance") =>
  apiGet(`/v3-1/live-exchange/tick?symbol=${symbol}&exchange=${exchange}`);

export const getLiveOrderbook = (symbol = "BTCUSDT", exchange = "binance") =>
  apiGet(`/v3-1/live-exchange/orderbook?symbol=${symbol}&exchange=${exchange}`);

export const getLiveCandles = (symbol = "BTCUSDT", exchange = "binance", timeframe = "1m", limit = 100) =>
  apiGet(`/v3-1/live-exchange/candles?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}&limit=${limit}`);

export const getLiveExchangeStatus = () =>
  apiGet("/v3-1/live-exchange/status");
