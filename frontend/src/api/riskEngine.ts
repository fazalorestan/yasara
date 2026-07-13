import { apiGet } from "./client";

export interface RiskEngineSummary {
  risk_level?: string;
  level?: string;
  exposure_percent?: number;
}

export interface SignalRisk {
  [key: string]: unknown;
}

export const getRiskEngineSummary = <T = RiskEngineSummary>() =>
  apiGet<T>("/v4-3/risk-engine/summary");

export const getSignalRisk = <T = SignalRisk>(symbol = "BTCUSDT", exchange = "binance", timeframe = "1m") =>
  apiGet<T>(`/v4-3/risk-engine/signal-risk?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);
