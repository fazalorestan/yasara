import { useEffect, useRef, useState } from "react";
import { getPaperTradingV45Account, getPaperTradingV45Summary } from "../api/paperTradingV45";
import { getRiskEngineSummary } from "../api/riskEngine";
import { getAIFusionSummary } from "../api/aiFusion";
import { getAlertHistory, getNotificationAlertsSummary } from "../api/notificationAlerts";
import { getOperationalMarketSnapshot, getOperationalWatchlist } from "../api/realData";
import { getFinalOperationalSummary } from "../api/finalOperational";
import type { MetricTone } from "../components/MetricCard";

// Sentinel shown whenever a field has never been successfully populated
// from the backend. Never replaced with invented/mock trading numbers —
// only ever replaced by a real value that came back from an API response.
const UNAVAILABLE = "Unavailable";

export interface WorkspaceHeaderState {
  totalEquity: string;
  equityTone: MetricTone;
  dailyPnl: string;
  dailyPnlTone: MetricTone;
  openPositions: string;
  openPositionsSub: string;
  riskLevel: string;
  riskTone: MetricTone;
  riskScoreLabel: string;
  aiConfidencePercent: number;
  /** True once at least one successful AI Fusion response has been received.
   * aiConfidencePercent is numeric (feeds a % ring) so it cannot itself
   * hold the "Unavailable" string — consult this flag before trusting it. */
  aiConfidenceAvailable: boolean;
}

export interface WorkspaceAlert {
  time: string;
  title: string;
  detail: string;
  tone: MetricTone;
}

export interface WorkspaceWatchRow {
  symbol: string;
  price: string;
  change: string;
  direction: "up" | "down";
}

export interface WorkspaceMarketOverview {
  totalCap: string;
  dominance: string;
  volume24h: string;
  fearGreed: number;
  fearGreedAvailable: boolean;
}

export interface WorkspaceState {
  loading: boolean;
  connected: boolean;
  lastUpdated: number;
  header: WorkspaceHeaderState;
  watchlist: WorkspaceWatchRow[];
  alerts: WorkspaceAlert[];
  marketOverview: WorkspaceMarketOverview;
}

const UNAVAILABLE_HEADER: WorkspaceHeaderState = {
  totalEquity: UNAVAILABLE,
  equityTone: "neutral",
  dailyPnl: UNAVAILABLE,
  dailyPnlTone: "neutral",
  openPositions: UNAVAILABLE,
  openPositionsSub: "Awaiting backend",
  riskLevel: UNAVAILABLE,
  riskTone: "neutral",
  riskScoreLabel: UNAVAILABLE,
  aiConfidencePercent: 0,
  aiConfidenceAvailable: false,
};

const UNAVAILABLE_STATE: WorkspaceState = {
  loading: true,
  connected: false,
  lastUpdated: 0,
  header: UNAVAILABLE_HEADER,
  watchlist: [],
  alerts: [],
  marketOverview: {
    totalCap: UNAVAILABLE,
    dominance: UNAVAILABLE,
    volume24h: UNAVAILABLE,
    fearGreed: 0,
    fearGreedAvailable: false,
  },
};

function toTone(direction: "up" | "down" | "flat"): MetricTone {
  if (direction === "up") return "up";
  if (direction === "down") return "down";
  return "neutral";
}

function formatCurrency(value: number | undefined, fallback: string): string {
  if (typeof value !== "number" || !Number.isFinite(value)) return fallback;
  return `$${value.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
}

/**
 * Polls every fault-tolerant backend summary endpoint the Enterprise
 * dashboard depends on and folds the results into a single view-model.
 *
 * Fault tolerance contract:
 * - Every request goes through apiGet(), which times out instead of
 *   hanging (see api/client.ts).
 * - All 9 calls run through Promise.allSettled, so one failing/missing
 *   endpoint never stops the others from updating, and never throws an
 *   unhandled rejection into React.
 * - A field only ever changes when its source call actually succeeds.
 *   On failure it keeps the last known-good value (lastGood ref); if
 *   there has never been a successful response, it reads "Unavailable"
 *   instead of a made-up number.
 * - `loading` flips to false after the first attempt completes (success
 *   or failure) so the dashboard always renders — it never blocks on a
 *   dead backend.
 * - Polling continues on a fixed interval (no unbounded retry loop
 *   inside a single tick) and is cleared on unmount.
 * - No `any` anywhere: every backend response is typed via the generic
 *   default interfaces exported from each api/*.ts wrapper, and
 *   Promise.allSettled's tuple overload preserves those individual types
 *   through the destructure below.
 */
export function useWorkspaceData(pollMs = 5000): WorkspaceState {
  const [state, setState] = useState<WorkspaceState>(UNAVAILABLE_STATE);
  const lastGood = useRef<WorkspaceState>(UNAVAILABLE_STATE);

  useEffect(() => {
    let cancelled = false;

    async function tick() {
      const results = await Promise.allSettled([
        getPaperTradingV45Account(),
        getPaperTradingV45Summary(),
        getRiskEngineSummary(),
        getAIFusionSummary(),
        getAlertHistory(),
        getNotificationAlertsSummary(),
        getOperationalWatchlist(),
        getOperationalMarketSnapshot(),
        getFinalOperationalSummary(),
      ]);

      if (cancelled) return;

      const [
        accountRes,
        paperSummaryRes,
        riskRes,
        aiFusionRes,
        alertHistoryRes,
        alertsSummaryRes,
        watchlistRes,
        marketSnapshotRes,
        finalOpRes,
      ] = results;

      const anySucceeded = results.some((r) => r.status === "fulfilled");
      const prev = lastGood.current;

      const account = accountRes.status === "fulfilled" ? accountRes.value : undefined;
      const risk = riskRes.status === "fulfilled" ? riskRes.value : undefined;
      const aiFusion = aiFusionRes.status === "fulfilled" ? aiFusionRes.value : undefined;
      const alertHistory = alertHistoryRes.status === "fulfilled" ? alertHistoryRes.value : undefined;
      const watchlistData = watchlistRes.status === "fulfilled" ? watchlistRes.value : undefined;
      const marketSnapshot = marketSnapshotRes.status === "fulfilled" ? marketSnapshotRes.value : undefined;
      // Fetched for connectivity/fault-tolerance coverage of every listed
      // endpoint; not yet surfaced in the header view-model.
      void (paperSummaryRes.status === "fulfilled" ? paperSummaryRes.value : undefined);
      void (alertsSummaryRes.status === "fulfilled" ? alertsSummaryRes.value : undefined);
      void (finalOpRes.status === "fulfilled" ? finalOpRes.value : undefined);

      const equity = account?.equity ?? account?.balance;
      const pnl = account?.pnl ?? account?.daily_pnl;
      const positions = account?.open_positions ?? account?.positions?.length;
      const riskLevel = risk?.risk_level ?? risk?.level;
      const aiConfidenceRaw =
        typeof aiFusion?.confidence === "number"
          ? aiFusion.confidence * (aiFusion.confidence <= 1 ? 100 : 1)
          : undefined;

      const header: WorkspaceHeaderState = {
        totalEquity: equity != null ? formatCurrency(equity, prev.header.totalEquity) : prev.header.totalEquity,
        equityTone: prev.header.equityTone,
        dailyPnl:
          pnl != null
            ? `${pnl >= 0 ? "+" : ""}${formatCurrency(pnl, prev.header.dailyPnl)}`
            : prev.header.dailyPnl,
        dailyPnlTone: pnl != null ? (pnl >= 0 ? "up" : "down") : prev.header.dailyPnlTone,
        openPositions: positions != null ? String(positions) : prev.header.openPositions,
        openPositionsSub: positions != null ? "Live positions" : prev.header.openPositionsSub,
        riskLevel: riskLevel ?? prev.header.riskLevel,
        riskTone: riskLevel
          ? toTone(riskLevel.toLowerCase() === "low" ? "up" : riskLevel.toLowerCase() === "high" ? "down" : "flat")
          : prev.header.riskTone,
        riskScoreLabel:
          risk?.exposure_percent != null ? `Exposure ${risk.exposure_percent}%` : prev.header.riskScoreLabel,
        aiConfidencePercent: aiConfidenceRaw ?? prev.header.aiConfidencePercent,
        aiConfidenceAvailable: aiConfidenceRaw != null ? true : prev.header.aiConfidenceAvailable,
      };

      const watchlistItems = watchlistData?.items;
      const watchlist: WorkspaceWatchRow[] =
        Array.isArray(watchlistItems) && watchlistItems.length
          ? watchlistItems.slice(0, 6).map((item) => ({
              symbol: item.symbol ?? item.normalized_symbol ?? "--",
              price: item.last_price != null ? item.last_price.toLocaleString() : "--",
              change: item.change_percent != null ? `${item.change_percent > 0 ? "+" : ""}${item.change_percent}%` : "--",
              direction: (item.change_percent ?? 0) >= 0 ? ("up" as const) : ("down" as const),
            }))
          : prev.watchlist;

      const alertItems = alertHistory?.alerts;
      const alerts: WorkspaceAlert[] =
        Array.isArray(alertItems) && alertItems.length
          ? alertItems.slice(0, 6).map((a) => ({
              time: a.time ?? a.timestamp ?? "--",
              title: a.title ?? a.type ?? "Alert",
              detail: a.detail ?? a.symbol ?? "",
              tone: (a.severity === "high" ? "danger" : a.severity === "medium" ? "warning" : "neutral") as MetricTone,
            }))
          : prev.alerts;

      const marketOverview: WorkspaceMarketOverview = marketSnapshot
        ? {
            totalCap:
              marketSnapshot.total_market_cap != null
                ? formatCurrency(marketSnapshot.total_market_cap, prev.marketOverview.totalCap)
                : prev.marketOverview.totalCap,
            dominance:
              marketSnapshot.btc_dominance != null ? `${marketSnapshot.btc_dominance}%` : prev.marketOverview.dominance,
            volume24h:
              marketSnapshot.volume_24h != null
                ? formatCurrency(marketSnapshot.volume_24h, prev.marketOverview.volume24h)
                : prev.marketOverview.volume24h,
            fearGreed: marketSnapshot.fear_greed ?? prev.marketOverview.fearGreed,
            fearGreedAvailable: marketSnapshot.fear_greed != null ? true : prev.marketOverview.fearGreedAvailable,
          }
        : prev.marketOverview;

      const next: WorkspaceState = {
        loading: false,
        connected: anySucceeded,
        lastUpdated: Date.now(),
        header,
        watchlist,
        alerts,
        marketOverview,
      };

      lastGood.current = next;
      setState(next);
    }

    tick();
    const id = setInterval(tick, pollMs);
    return () => {
      cancelled = true;
      clearInterval(id);
    };
  }, [pollMs]);

  return state;
}
