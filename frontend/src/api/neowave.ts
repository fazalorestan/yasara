import { apiGet } from "./client";
export const getNeoWaveSummary = () => apiGet("/v4-15/neowave/summary");
export const getNeoWaveQuick = (symbol = "BTCUSDT", exchange = "binance", timeframe = "1m") =>
  apiGet(`/v4-15/neowave/quick?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);
export const getEngineRegistryPro = () => apiGet("/v4-15/neowave/engine-registry");
