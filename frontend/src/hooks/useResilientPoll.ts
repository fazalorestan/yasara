import { useEffect, useRef, useState } from "react";

export interface ResilientPollState<T> {
  /** Last known-good value, or null if we have never successfully fetched one. */
  data: T | null;
  /** True if `data` is non-null (either fresh or cached from a previous success). */
  available: boolean;
  /** True only until the very first attempt resolves (success or failure). */
  loading: boolean;
  /** True if `data` is a cached value and the most recent attempt failed. */
  stale: boolean;
}

export interface ResilientPollOptions {
  /** Polling interval while requests are succeeding. Default 8000ms. */
  baseIntervalMs?: number;
  /** Ceiling for the backoff interval while requests keep failing. Default 45000ms. */
  maxIntervalMs?: number;
  /** Re-subscribe when any of these change, same semantics as a useEffect dep array. */
  deps?: unknown[];
}

/**
 * Polls `fetcher` on a resilient schedule:
 * - never throws out of the hook (all errors are swallowed after being recorded)
 * - never blocks rendering (first render is `loading`, never suspends)
 * - backs off exponentially (up to maxIntervalMs) while the endpoint is failing,
 *   instead of hammering an unavailable backend
 * - keeps showing the last known-good value (`stale: true`) rather than inventing data
 * - reports `available: false` (and `data: null`) when there has never been a
 *   successful response, so the UI can render an explicit "Unavailable" state
 */
export function useResilientPoll<T>(fetcher: () => Promise<T>, opts: ResilientPollOptions = {}): ResilientPollState<T> {
  const { baseIntervalMs = 8000, maxIntervalMs = 45000 } = opts;
  const deps = opts.deps ?? [];

  const [state, setState] = useState<ResilientPollState<T>>({
    data: null,
    available: false,
    loading: true,
    stale: false,
  });

  const fetcherRef = useRef(fetcher);
  fetcherRef.current = fetcher;

  useEffect(() => {
    let cancelled = false;
    let currentInterval = baseIntervalMs;
    let timer: ReturnType<typeof setTimeout> | null = null;
    let cache: T | null = null;

    async function run() {
      try {
        const result = await fetcherRef.current();
        if (cancelled) return;
        cache = result;
        currentInterval = baseIntervalMs;
        setState({ data: result, available: true, loading: false, stale: false });
      } catch {
        if (cancelled) return;
        currentInterval = Math.min(currentInterval * 2, maxIntervalMs);
        setState({ data: cache, available: cache != null, loading: false, stale: cache != null });
      } finally {
        if (!cancelled) {
          timer = setTimeout(run, currentInterval);
        }
      }
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
