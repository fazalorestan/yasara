import { apiGet } from "./client";

export const getBacktestBenchmarkSummary = () =>
  apiGet("/v4-4/backtest-benchmark/summary");

export const getBenchmarkHistory = () =>
  apiGet("/v4-4/backtest-benchmark/benchmark/history");
