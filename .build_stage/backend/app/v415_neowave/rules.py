class NeoWaveRuleRegistryV415:
    def __init__(self):
        self.rules = {
            "minimum_wave_count": {"enabled": True, "min": 3},
            "alternating_direction": {"enabled": True},
            "price_progression": {"enabled": True},
            "time_progression": {"enabled": True},
            "complexity_ready": {"enabled": False, "planned": "v4.16"},
        }

    def list(self):
        return {"ready": True, "rules": self.rules, "count": len(self.rules)}

    def validate_minimum_count(self, waves):
        return len(waves) >= self.rules["minimum_wave_count"]["min"]

    def validate_alternating_direction(self, waves):
        if len(waves) < 2:
            return False
        ok = 0
        for i in range(1, len(waves)):
            if waves[i]["direction"] != waves[i-1]["direction"]:
                ok += 1
        return ok >= max(1, len(waves) - 2)

    def validate_price_progression(self, waves):
        if not waves:
            return False
        return all(w.get("price_change_abs", 0) >= 0 for w in waves)

    def validate_time_progression(self, waves):
        if not waves:
            return False
        return all(w.get("duration", 0) >= 0 for w in waves)

    def validate(self, waves):
        checks = {
            "minimum_wave_count": self.validate_minimum_count(waves),
            "alternating_direction": self.validate_alternating_direction(waves),
            "price_progression": self.validate_price_progression(waves),
            "time_progression": self.validate_time_progression(waves),
        }
        passed = sum(1 for v in checks.values() if v)
        confidence = round(passed / max(len(checks), 1) * 100, 2)
        return {"valid": confidence >= 60, "confidence": confidence, "checks": checks}
