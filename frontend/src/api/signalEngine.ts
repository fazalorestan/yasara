import { apiGet } from "./client";

export const getSignalEngineSummary = () =>
  apiGet("/v4-2/signal-engine/summary");

export const getSignalEngineQuick = (symbol = "BTCUSDT", exchange = "binance", timeframe = "1m") =>
  apiGet(`/v4-2/signal-engine/quick?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);
