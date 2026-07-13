import { apiGet } from "./client";

export const getExchangeConnectorSummary = () =>
  apiGet("/v2-3/exchange-connector/summary");

export const getExchangeCapabilities = () =>
  apiGet("/v2-3/exchange-connector/capabilities");

export const getExchangeQuote = (symbol = "BTCUSDT", exchange = "binance") =>
  apiGet(`/v2-3/exchange-connector/quote?symbol=${symbol}&exchange=${exchange}`);

export const getExchangeOhlc = (symbol = "BTCUSDT", exchange = "binance", timeframe = "4H", limit = 120) =>
  apiGet(`/v2-3/exchange-connector/ohlc?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}&limit=${limit}`);

export const getExchangeOrderbook = (symbol = "BTCUSDT", exchange = "binance") =>
  apiGet(`/v2-3/exchange-connector/orderbook?symbol=${symbol}&exchange=${exchange}`);
