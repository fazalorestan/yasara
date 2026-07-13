import { useEffect, useRef, useState } from "react";

export type ResourceStatus = "Live" | "Unavailable";

export interface ResilientResourceState<T> {
  /** Last known-good value, or null if nothing has ever been received. */
  data: T | null;
  /** false whenever there is no data to show - drives every widget's empty state. */
  available: boolean;
  /** Human-readable status matching the required normalized shape. */
  status: ResourceStatus;
  /** True only until the first attempt resolves (success or failure). */
  loading: boolean;
  /** True if `data` is cached from a previous success and the latest attempt failed. */
  stale: boolean;
}

export interface ResilientResourceOptions {
  /** Poll cadence while requests are succeeding. Default 8000ms. */
  baseIntervalMs?: number;
  /** Ceiling for backoff while an endpoint keeps failing. Default 45000ms. */
  maxIntervalMs?: number;
  /** Re-subscribe when any of these change. */
  deps?: unknown[];
}

/**
 * The single shared resilient-fetch hook every dashboard widget uses.
 *
 * `fetcher` is expected to be built on top of apiGet() (see api/client.ts),
 * which never throws to the caller in a way that crashes the UI - it
 * rejects with a typed ApiError on timeout, network error, non-2xx
 * status, or malformed JSON, and this hook catches that rejection here.
 *
 * - Never throws, never blocks rendering (first render is `loading`).
 * - Polls on a fixed, bounded cadence - no runaway retry loops. Backs off
 *   exponentially (up to maxIntervalMs) while an endpoint keeps failing.
 * - Keeps the last known-good value (`stale: true`) instead of ever
 *   inventing/mocking data when a later poll fails.
 * - Reports the exact normalized failure shape widgets should render
 *   against: `available: false`, `status: "Unavailable"`, `data: null`
 *   whenever nothing has ever been received successfully.
 * - Skips a tick if the previous one is still in flight, so a slow/hung
 *   endpoint can't cause overlapping requests to pile up.
 */
export function useResilientResource<T>(
  fetcher: () => Promise<T | null>,
  opts: ResilientResourceOptions = {}
): ResilientResourceState<T> {
  const { baseIntervalMs = 8000, maxIntervalMs = 45000 } = opts;
  const deps = opts.deps ?? [];

  const [state, setState] = useState<ResilientResourceState<T>>({
    data: null,
    available: false,
    status: "Unavailable",
    loading: true,
    stale: false,
  });

  const fetcherRef = useRef(fetcher);
  fetcherRef.current = fetcher;
  const inFlight = useRef(false);

  useEffect(() => {
    let cancelled = false;
    let currentInterval = baseIntervalMs;
    let timer: ReturnType<typeof setTimeout> | null = null;
    let cache: T | null = null;

    async function run() {
      if (inFlight.current) return; // never let ticks pile up
      inFlight.current = true;

      let result: T | null = null;
      try {
        result = await fetcherRef.current();
      } catch {
        // Defense-in-depth only: apiGet-based fetchers reject with a typed
        // ApiError rather than throwing arbitrarily, but a widget must
        // never crash even if a future fetcher regresses.
        result = null;
      }

      inFlight.current = false;
      if (cancelled) return;

      if (result != null) {
        cache = result;
        currentInterval = baseIntervalMs;
        setState({ data: result, available: true, status: "Live", loading: false, stale: false });
      } else {
        currentInterval = Math.min(currentInterval * 2, maxIntervalMs);
        setState({
          data: cache,
          available: cache != null,
          status: cache != null ? "Live" : "Unavailable",
          loading: false,
          stale: cache != null,
        });
      }

      if (!cancelled) timer = setTimeout(run, currentInterval);
    }

    run();
    return () => {
      cancelled = true;
      if (timer) clearTimeout(timer);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps);

  return state;
}
