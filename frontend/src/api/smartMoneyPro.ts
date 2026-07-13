import { apiGet } from "./client";
export const getSmartMoneyProSummary = () => apiGet("/v4-11/smart-money-pro/summary");
export const getSmartMoneyProQuick = (symbol = "BTCUSDT", exchange = "binance", timeframe = "1m") =>
  apiGet(`/v4-11/smart-money-pro/quick?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);
