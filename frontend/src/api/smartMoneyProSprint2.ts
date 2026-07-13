import { apiGet } from "./client";
export const getSmartMoneyProSprint2Summary = () => apiGet("/v4-12/smart-money-pro-sprint2/summary");
export const getSmartMoneyProSprint2Quick = (symbol = "BTCUSDT", exchange = "binance", timeframe = "1m") =>
  apiGet(`/v4-12/smart-money-pro-sprint2/quick?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);
