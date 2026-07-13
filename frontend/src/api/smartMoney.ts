import { apiGet } from "./client";

export const getSmartMoneySummary = () =>
  apiGet("/v3-5/smart-money/summary");

export const getSmartMoneyQuick = (symbol = "BTCUSDT", exchange = "binance", timeframe = "1m") =>
  apiGet(`/v3-5/smart-money/quick?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);
