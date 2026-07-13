class SignalReasonBuilder:
    def build(self, composite: dict):
        reasons = []
        for part in composite.get("parts", {}).values():
            reason = part.get("reason")
            if reason:
                reasons.append(reason)
        return reasons or ["no_clear_signal"]

signal_reason_builder = SignalReasonBuilder()
