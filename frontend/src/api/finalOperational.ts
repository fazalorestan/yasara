import { apiGet } from "./client";

export interface FinalOperationalSummary {
  [key: string]: unknown;
}

export interface FinalOperationalHealth {
  latency_ms?: number;
  data_rate_mbps?: number;
  connections?: number;
  cpu_percent?: number;
  memory_percent?: number;
  disk_percent?: number;
  uptime?: string;
  mode?: string;
}

export interface FinalOperationalModules {
  [key: string]: unknown;
}

export interface FinalOperationalDashboard {
  [key: string]: unknown;
}

export interface FinalOperationalReleaseGate {
  [key: string]: unknown;
}

export const getFinalOperationalSummary = <T = FinalOperationalSummary>() =>
  apiGet<T>("/v2-6/final-operational/summary");

export const getFinalOperationalHealth = <T = FinalOperationalHealth>() =>
  apiGet<T>("/v2-6/final-operational/health");

export const getFinalOperationalModules = <T = FinalOperationalModules>() =>
  apiGet<T>("/v2-6/final-operational/modules");

export const getFinalOperationalDashboard = <T = FinalOperationalDashboard>(
  symbol = "BTCUSDT",
  exchange = "binance",
  timeframe = "4H"
) => apiGet<T>(`/v2-6/final-operational/dashboard?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);

export const getFinalOperationalReleaseGate = <T = FinalOperationalReleaseGate>() =>
  apiGet<T>("/v2-6/final-operational/release-gate");
