import { apiGet } from "./client";
export const getElliottSummary = () => apiGet("/v4-17/elliott/summary");
export const getElliottQuick = (symbol = "BTCUSDT", exchange = "binance", timeframe = "1m") =>
  apiGet(`/v4-17/elliott/quick?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);
