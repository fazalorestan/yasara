class FakeExchangePublicClient:
    def __init__(self, ticker_payload: dict | None = None, order_book_payload: dict | None = None):
        self.calls = []
        self.ticker_payload = ticker_payload or {
            "data": {
                "lastPrice": "100",
                "priceChangePercent": "1",
                "volume": "10",
            }
        }
        self.order_book_payload = order_book_payload or {
            "data": {
                "bids": [["100", "1"]],
                "asks": [["101", "2"]],
            }
        }

    async def get_json(self, url: str, params: dict | None = None):
        self.calls.append((url, params or {}))
        if "depth" in url or "book" in url:
            return self.order_book_payload
        return self.ticker_payload
