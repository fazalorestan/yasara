class WalkForwardService:
    def windows(self, total_bars: int = 120, train_size: int = 40, test_size: int = 20):
        result = []
        start = 0
        while start + train_size + test_size <= total_bars:
            result.append({"train_start": start, "train_end": start + train_size - 1, "test_start": start + train_size, "test_end": start + train_size + test_size - 1})
            start += test_size
        return {"ready": True, "windows": result, "count": len(result)}

    def summarize(self):
        windows = self.windows()
        return {"ready": True, "window_count": windows["count"], "stable": windows["count"] >= 3}

walk_forward_service = WalkForwardService()
