import { apiGet } from "./client";

export const getMarketStructureProSummary = () =>
  apiGet("/v4-21/market-structure-pro/summary");

export const getMarketStructureProQuick = (
  symbol = "BTCUSDT",
  exchange = "binance",
  timeframe = "15m"
) =>
  apiGet(`/v4-21/market-structure-pro/quick?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);
