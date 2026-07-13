import { apiGet } from "./client";

export const getAdvancedAiIndicatorsSummary = () =>
  apiGet("/v3-2/ai-indicators/summary");

export const getAdvancedAiQuick = (symbol = "BTCUSDT", exchange = "binance", timeframe = "1m", limit = 120) =>
  apiGet(`/v3-2/ai-indicators/quick?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}&limit=${limit}`);

export const getAdvancedAiBatch = () =>
  apiGet("/v3-2/ai-indicators/batch");
