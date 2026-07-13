import { apiGet } from "./client";
export const getMarketStructureSprint2Summary = () => apiGet("/v4-10/market-structure-sprint2/summary");
export const getMarketStructureSprint2Quick = (symbol = "BTCUSDT", exchange = "binance") =>
  apiGet(`/v4-10/market-structure-sprint2/quick?symbol=${symbol}&exchange=${exchange}`);
