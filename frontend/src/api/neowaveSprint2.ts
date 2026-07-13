import { apiGet } from "./client";
export const getNeoWaveSprint2Summary = () => apiGet("/v4-16/neowave-sprint2/summary");
export const getNeoWaveSprint2Quick = (symbol = "BTCUSDT", exchange = "binance", timeframe = "1m") =>
  apiGet(`/v4-16/neowave-sprint2/quick?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);
