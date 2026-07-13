class ElliottRuleRegistryV417:
    def __init__(self):
        self.rules = {
            "wave_2_not_beyond_wave_1_start": {"enabled": True},
            "wave_3_not_shortest": {"enabled": True},
            "wave_4_not_overlap_wave_1": {"enabled": True},
            "abc_has_three_waves": {"enabled": True},
            "fib_base_validation": {"enabled": True},
        }

    def list(self):
        return {"ready": True, "rules": self.rules, "count": len(self.rules)}

    def validate_impulse(self, waves):
        checks = {
            "has_five_waves": len(waves) >= 5,
            "wave_2_not_beyond_wave_1_start": True,
            "wave_3_not_shortest": True,
            "wave_4_not_overlap_wave_1": True,
        }
        if len(waves) >= 5:
            w1, w2, w3, w4, w5 = waves[:5]
            bullish = w1["direction"] == "up"
            if bullish:
                checks["wave_2_not_beyond_wave_1_start"] = w2["to"]["price"] > w1["from"]["price"]
                checks["wave_4_not_overlap_wave_1"] = w4["to"]["price"] > w1["to"]["price"]
            else:
                checks["wave_2_not_beyond_wave_1_start"] = w2["to"]["price"] < w1["from"]["price"]
                checks["wave_4_not_overlap_wave_1"] = w4["to"]["price"] < w1["to"]["price"]
            lengths = [w1["price_change_abs"], w3["price_change_abs"], w5["price_change_abs"]]
            checks["wave_3_not_shortest"] = w3["price_change_abs"] >= min(lengths)
        passed = sum(1 for v in checks.values() if v)
        score = round(passed / max(len(checks), 1) * 100, 2)
        return {"valid": score >= 75, "score": score, "checks": checks}

    def validate_correction(self, waves):
        checks = {
            "has_three_waves": len(waves) >= 3,
            "abc_alternates": True,
        }
        if len(waves) >= 3:
            a, b, c = waves[:3]
            checks["abc_alternates"] = a["direction"] != b["direction"] and b["direction"] != c["direction"]
        passed = sum(1 for v in checks.values() if v)
        score = round(passed / max(len(checks), 1) * 100, 2)
        return {"valid": score >= 70, "score": score, "checks": checks}
