// YaSara Enterprise Platform — hardened API client
// Every request in the app funnels through apiGet() below, so this is the
// single choke point for fault tolerance: timeout, abort, and typed
// failures. No backend files, routes, or contracts are touched — this
// only changes how the frontend behaves when a call does not succeed.

export const API_BASE = "/api/v1";

/** Default per-request timeout. Keeps a slow/hanging endpoint from ever
 * blocking the dashboard — the request is aborted and treated as
 * unavailable instead of hanging indefinitely. */
export const DEFAULT_TIMEOUT_MS = 6000;

export type ApiErrorReason = "timeout" | "network" | "http" | "parse";

/** Typed, catchable failure. Never an uncaught exception at the UI layer —
 * every caller in this app awaits apiGet() inside Promise.allSettled, so a
 * thrown ApiError simply resolves that slot as "rejected" and the caller
 * decides what to show (cached value or "Unavailable"). */
export class ApiError extends Error {
  readonly reason: ApiErrorReason;
  readonly status?: number;
  readonly path: string;

  constructor(reason: ApiErrorReason, path: string, message: string, status?: number) {
    super(message);
    this.name = "ApiError";
    this.reason = reason;
    this.path = path;
    this.status = status;
  }
}

export function isApiError(error: unknown): error is ApiError {
  return error instanceof ApiError;
}

/**
 * Fetch JSON from the backend with a hard timeout and no throw-on-network-
 * failure surprises. Resolves with typed data on success; rejects with a
 * typed ApiError (never a bare Error/DOMException) on any failure so
 * callers can branch on `.reason` if they want to.
 *
 * `T` defaults to `unknown` (never `any`) so a caller that forgets to
 * specify a shape is forced to narrow the result before using it, instead
 * of silently getting an untyped value.
 *
 * Does NOT retry internally — one bounded attempt per call. Callers that
 * poll (e.g. useWorkspaceData) are responsible for their own interval;
 * this function guarantees that a single attempt always settles within
 * `timeoutMs` instead of hanging forever.
 */
export async function apiGet<T = unknown>(path: string, timeoutMs: number = DEFAULT_TIMEOUT_MS): Promise<T> {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);

  let response: Response;
  try {
    response = await fetch(`${API_BASE}${path}`, { signal: controller.signal });
  } catch (err) {
    clearTimeout(timer);
    if (err instanceof DOMException && err.name === "AbortError") {
      throw new ApiError("timeout", path, `Request timed out after ${timeoutMs}ms: ${path}`);
    }
    throw new ApiError("network", path, `Network error while requesting ${path}`);
  }
  clearTimeout(timer);

  if (!response.ok) {
    throw new ApiError("http", path, `API request failed (${response.status}): ${path}`, response.status);
  }

  try {
    return (await response.json()) as T;
  } catch {
    throw new ApiError("parse", path, `Failed to parse JSON response from ${path}`);
  }
}
