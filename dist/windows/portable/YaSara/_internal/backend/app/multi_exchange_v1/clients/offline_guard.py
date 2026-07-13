class OfflineNetworkGuardClientV1:
    async def get_json(self, url: str, params: dict | None = None) -> dict:
        raise RuntimeError(
            "Network access is disabled for unit tests. "
            "Use FakeClient or mark the test as integration."
        )
