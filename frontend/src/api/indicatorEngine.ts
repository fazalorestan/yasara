import { apiGet } from "./client";

export const getIndicatorEngineSummary = () =>
  apiGet("/v4-1/indicator-engine/summary");

export const getIndicatorEngineRegistry = () =>
  apiGet("/v4-1/indicator-engine/registry");

export const getIndicatorEngineQuick = (symbol = "BTCUSDT", exchange = "binance", timeframe = "1m") =>
  apiGet(`/v4-1/indicator-engine/quick?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);
