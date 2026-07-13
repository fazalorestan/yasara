import { apiGet } from "./client";

export const getStrategyBuilderSummary = () =>
  apiGet("/v3-3/strategy-builder/summary");

export const getStrategies = () =>
  apiGet("/v3-3/strategy-builder/strategies");

export const getStrategyContext = (symbol = "BTCUSDT", exchange = "binance", timeframe = "1m") =>
  apiGet(`/v3-3/strategy-builder/context?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);
