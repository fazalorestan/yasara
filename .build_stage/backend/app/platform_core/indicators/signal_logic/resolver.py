class SignalDirectionResolver:
    def resolve(self, composite: dict):
        parts = composite.get("parts", {})
        trend = parts.get("trend", {}).get("direction", "WAIT")
        momentum = parts.get("momentum", {}).get("direction", "WAIT")
        score = int(composite.get("score", 0))

        if score < 45:
            return "WAIT"
        if trend == momentum and trend in ["LONG", "SHORT"]:
            return trend
        if trend in ["LONG", "SHORT"] and momentum == "WAIT":
            return trend
        return "WAIT"

signal_direction_resolver = SignalDirectionResolver()
