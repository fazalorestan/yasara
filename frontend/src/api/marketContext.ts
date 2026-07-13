import { apiGet } from "./client";

export const getMarketContextSummary = () =>
  apiGet("/v4-0/market-context/summary");

export const getMarketContextQuick = (symbol = "BTCUSDT", exchange = "binance") =>
  apiGet(`/v4-0/market-context/quick?symbol=${symbol}&exchange=${exchange}`);

export const getMarketContextEngines = () =>
  apiGet("/v4-0/market-context/engines");
