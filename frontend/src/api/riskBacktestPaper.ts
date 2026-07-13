import { apiGet } from "./client";

export const getRiskBacktestPaperSummary = () =>
  apiGet("/v2-5/risk-backtest-paper/summary");

export const getBacktestResult = (symbol = "BTCUSDT", exchange = "binance", timeframe = "4H") =>
  apiGet(`/v2-5/risk-backtest-paper/backtest?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);

export const getPaperState = () =>
  apiGet("/v2-5/risk-backtest-paper/paper-state");
