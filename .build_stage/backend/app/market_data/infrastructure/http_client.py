import asyncio
import time
from typing import Any
import httpx

class ExchangeHttpError(Exception):
    pass

class ExchangeRateLimitError(ExchangeHttpError):
    pass

class ExchangeUnavailableError(ExchangeHttpError):
    pass

class AsyncExchangeHttpClient:
    def __init__(
        self,
        base_url: str,
        timeout_seconds: float = 15,
        max_retries: int = 3,
        backoff_base_seconds: float = 0.35,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds
        self.max_retries = max_retries
        self.backoff_base_seconds = backoff_base_seconds
        self.client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=httpx.Timeout(timeout_seconds),
            limits=httpx.Limits(max_connections=100, max_keepalive_connections=30),
            headers={"User-Agent": "YaSara/1.0"},
        )

    async def request(self, method: str, path: str, params: dict[str, Any] | None = None) -> Any:
        last_error: Exception | None = None
        for attempt in range(self.max_retries + 1):
            start = time.perf_counter()
            try:
                response = await self.client.request(method, path, params=params)
                latency_ms = (time.perf_counter() - start) * 1000
                if response.status_code == 429:
                    raise ExchangeRateLimitError("Exchange rate limit reached")
                if response.status_code >= 500:
                    raise ExchangeUnavailableError(f"Exchange unavailable: {response.status_code}")
                if response.status_code >= 400:
                    raise ExchangeHttpError(f"Exchange error {response.status_code}: {response.text}")
                data = response.json()
                if isinstance(data, dict):
                    data.setdefault("_yasara_latency_ms", latency_ms)
                return data
            except (httpx.TimeoutException, httpx.TransportError, ExchangeRateLimitError, ExchangeUnavailableError) as exc:
                last_error = exc
                if attempt >= self.max_retries:
                    raise
                await asyncio.sleep(self.backoff_base_seconds * (2 ** attempt))
        if last_error:
            raise last_error
        raise ExchangeHttpError("Unknown HTTP error")

    async def close(self) -> None:
        await self.client.aclose()
