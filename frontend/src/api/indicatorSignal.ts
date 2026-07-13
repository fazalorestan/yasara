import { apiGet } from "./client";

export const getIndicatorSignalSummary = () =>
  apiGet("/v2-4/indicator-signal/summary");

export const getIndicatorSnapshot = (symbol = "BTCUSDT", exchange = "binance", timeframe = "4H") =>
  apiGet(`/v2-4/indicator-signal/snapshot?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);

export const getIndicatorBatch = (exchange = "all") =>
  apiGet(`/v2-4/indicator-signal/batch?exchange=${exchange}`);
