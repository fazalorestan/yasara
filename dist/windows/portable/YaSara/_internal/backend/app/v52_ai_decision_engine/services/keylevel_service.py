class KeyLevelService:
    ALLOWED = {"support","resistance","vwap","poc","liquidity","daily_high","daily_low","weekly_high","weekly_low"}
    def normalize(self, payload: dict):
        return {k: payload.get(k) for k in self.ALLOWED if k in payload}
