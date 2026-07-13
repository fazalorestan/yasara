import { apiGet } from "./client";
export const getICTEngineSummary = () => apiGet("/v4-13/ict-engine/summary");
export const getICTEngineQuick = (symbol = "BTCUSDT", exchange = "binance", timeframe = "1m") =>
  apiGet(`/v4-13/ict-engine/quick?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);
