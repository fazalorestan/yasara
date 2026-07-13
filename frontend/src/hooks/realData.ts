import { apiGet } from "./client";

// Default shapes for callers that don't need a specific type. Any caller
// (e.g. a component using useResilientResource<CustomShape>) can still
// request its own shape via the generic parameter — these are defaults,
// not a hard lock — so this file's typing never fights a component's own
// local interface for the same endpoint.

export interface UserSettingsV21 {
  theme: string;
  workspace: string;
  default_exchange: string;
  default_symbol: string;
  language: string;
  live_trading_enabled: boolean;
}

export interface WatchlistItemV21 {
  symbol: string;
  exchange: string;
  favorite: boolean;
}

export interface WatchlistStateV21 {
  items: WatchlistItemV21[];
}

export interface OperationalMarketSnapshot {
  ready: boolean;
  exchange: string;
  count: number;
  items: Array<{
    symbol: string;
    normalized_symbol: string;
    exchange: string;
    last_price: number;
    spread: number;
    favorite: boolean;
    source: string;
  }>;
}

export const getOperationalSettings = <T = UserSettingsV21>() =>
  apiGet<T>("/v2-1/real-data/settings");

export const getOperationalWatchlist = <T = WatchlistStateV21>() =>
  apiGet<T>("/v2-1/real-data/watchlist");

export const getOperationalMarketSnapshot = <T = OperationalMarketSnapshot>(exchange = "all") =>
  apiGet<T>(`/v2-1/real-data/market-snapshot?exchange=${exchange}`);
