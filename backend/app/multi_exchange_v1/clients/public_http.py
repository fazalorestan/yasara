import httpx

class PublicHTTPClientV1:
    def __init__(self, timeout: float = 10.0):
        self.timeout = timeout

    async def get_json(self, url: str, params: dict | None = None) -> dict:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data if isinstance(data, dict) else {"data": data}
