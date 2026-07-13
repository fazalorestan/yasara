class FeatureUsageCounter:
    def __init__(self):
        self._usage = {}

    def increment(self, feature: str, amount: int = 1):
        self._usage[feature] = self._usage.get(feature, 0) + amount
        return {"feature": feature, "count": self._usage[feature]}

    def snapshot(self):
        return {"ready": True, "usage": dict(self._usage)}

    def reset(self):
        self._usage = {}
        return {"ready": True, "usage": {}}

feature_usage_counter = FeatureUsageCounter()
