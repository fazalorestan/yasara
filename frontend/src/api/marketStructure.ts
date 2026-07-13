import { apiGet } from "./client";

export const getMarketStructureSummary = () =>
  apiGet("/v4-9/market-structure/summary");

export const getMarketStructureQuick = (symbol = "BTCUSDT", exchange = "binance", timeframe = "1m") =>
  apiGet(`/v4-9/market-structure/quick?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);
