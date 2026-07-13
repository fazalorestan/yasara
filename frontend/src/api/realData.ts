import { apiGet } from "./client";

// Default shapes for callers that don't need a specific type. Any caller
// (e.g. a component using useResilientResource<CustomShape>) can still
// request its own shape via the generic parameter — these are defaults,
// not a hard lock — so this file's typing never fights a component's own
// local interface for the same endpoint. All fields are optional because
// an endpoint that is down or partially degraded may legitimately omit
// any of them; that's exactly the "Unavailable" case the rest of the app
// is built to handle gracefully, not a type error.

export interface UserSettingsV21 {
  theme?: string;
  workspace?: string;
  default_exchange?: string;
  default_symbol?: string;
  language?: string;
  live_trading_enabled?: boolean;
}

export interface WatchlistItemV21 {
  symbol?: string;
  normalized_symbol?: string;
  exchange?: string;
  favorite?: boolean;
  last_price?: number;
  change_percent?: number;
}

export interface WatchlistStateV21 {
  items?: WatchlistItemV21[];
}

export interface OperationalMarketSnapshotItem {
  symbol?: string;
  normalized_symbol?: string;
  exchange?: string;
  last_price?: number;
  spread?: number;
  favorite?: boolean;
  source?: string;
}

export interface OperationalMarketSnapshot {
  ready?: boolean;
  exchange?: string;
  count?: number;
  total_market_cap?: number;
  btc_dominance?: number;
  volume_24h?: number;
  fear_greed?: number;
  high_24h?: number;
  low_24h?: number;
  change_24h_percent?: number;
  market_trend?: string;
  altcoin_season_index?: number;
  items?: OperationalMarketSnapshotItem[];
}

export const getOperationalSettings = <T = UserSettingsV21>() =>
  apiGet<T>("/v2-1/real-data/settings");

export const getOperationalWatchlist = <T = WatchlistStateV21>() =>
  apiGet<T>("/v2-1/real-data/watchlist");

export const getOperationalMarketSnapshot = <T = OperationalMarketSnapshot>(exchange = "all") =>
  apiGet<T>(`/v2-1/real-data/market-snapshot?exchange=${exchange}`);
