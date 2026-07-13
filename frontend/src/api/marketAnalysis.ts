import { apiGet } from "./client";

export const getMarketAnalysisSummary = () =>
  apiGet("/v3-4/market-analysis/summary");

export const getMarketAnalysisQuick = (symbol = "BTCUSDT", exchange = "binance") =>
  apiGet(`/v3-4/market-analysis/quick?symbol=${symbol}&exchange=${exchange}`);
