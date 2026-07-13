export const API_BASE = "/api/v1";

export type ApiErrorKind = "timeout" | "network" | "http" | "parse";

export class ApiError extends Error {
  kind: ApiErrorKind;
  status?: number;

  constructor(message: string, kind: ApiErrorKind, status?: number) {
    super(message);
    this.name = "ApiError";
    this.kind = kind;
    this.status = status;
  }
}

const DEFAULT_TIMEOUT_MS = 6000;

/**
 * Same external contract as before: resolves with T on success, throws on failure.
 * Internally every request now has a hard timeout and is abortable, so a hung or
 * unavailable backend endpoint can never leave a caller waiting indefinitely.
 */
export async function apiGet<T>(path: string, timeoutMs: number = DEFAULT_TIMEOUT_MS): Promise<T> {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);

  try {
    let response: Response;
    try {
      response = await fetch(`${API_BASE}${path}`, { signal: controller.signal });
    } catch (err: any) {
      if (err?.name === "AbortError") {
        throw new ApiError(`Request timed out: ${path}`, "timeout");
      }
      throw new ApiError(`Network error: ${path}`, "network");
    }

    if (!response.ok) {
      throw new ApiError(`API request failed: ${path} (${response.status})`, "http", response.status);
    }

    try {
      return (await response.json()) as T;
    } catch {
      throw new ApiError(`Invalid JSON response: ${path}`, "parse");
    }
  } finally {
    clearTimeout(timer);
  }
}
