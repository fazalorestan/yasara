import { apiGet } from "./client";

export interface AIFusionSummary {
  confidence?: number;
  decision?: string;
  bias?: string;
  strength?: string;
  timeframe?: string;
  strategy?: string;
}

export interface AIFusionQuick {
  [key: string]: unknown;
}

export const getAIFusionSummary = <T = AIFusionSummary>() =>
  apiGet<T>("/v4-14/ai-fusion/summary");

export const getAIFusionQuick = <T = AIFusionQuick>(symbol = "BTCUSDT", exchange = "binance", timeframe = "1m") =>
  apiGet<T>(`/v4-14/ai-fusion/quick?symbol=${symbol}&exchange=${exchange}&timeframe=${timeframe}`);
