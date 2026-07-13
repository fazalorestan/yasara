import { apiGet } from "./client";

export interface PaperTradingPosition {
  symbol?: string;
  side?: string;
  size?: number;
  entry_price?: number;
  pnl?: number;
  pnl_percent?: number;
  [key: string]: unknown;
}

export interface PaperTradingAccount {
  equity?: number;
  balance?: number;
  pnl?: number;
  daily_pnl?: number;
  open_positions?: number;
  positions?: PaperTradingPosition[];
}

export interface PaperTradingSummary {
  [key: string]: unknown;
}

export const getPaperTradingV45Summary = <T = PaperTradingSummary>() =>
  apiGet<T>("/v4-5/paper-trading/summary");

export const getPaperTradingV45Account = <T = PaperTradingAccount>() =>
  apiGet<T>("/v4-5/paper-trading/account");
