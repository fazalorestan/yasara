class LiveDataHistoryBuffer:
    def append(self, symbol: str = "BTCUSDT", limit: int = 5):
        rows = [{"symbol": symbol, "price": 50000.0 + i, "timestamp": i} for i in range(limit)]
        return {"ready": True, "symbol": symbol, "history": rows, "count": len(rows)}

    def latest(self, symbol: str = "BTCUSDT"):
        history = self.append(symbol)["history"]
        return {"ready": True, "symbol": symbol, "latest": history[-1]}

live_data_history_buffer = LiveDataHistoryBuffer()
