import hashlib


class AutoTradeGateV40:
    # Demo license hashes. Replace with secure server-side license validation later.
    VALID_LICENSE_HASHES = {
        hashlib.sha256("YASARA-PERSONAL-RASOUL-2026".encode()).hexdigest()
    }

    def hash_key(self, key: str):
        return hashlib.sha256((key or "").strip().encode()).hexdigest()

    def validate(self, request):
        reasons = []

        if request.build_type != "personal":
            reasons.append("auto_trade_allowed_only_in_personal_build")

        if self.hash_key(request.license_key) not in self.VALID_LICENSE_HASHES:
            reasons.append("invalid_personal_license_key")

        if not request.has_exchange_api_key:
            reasons.append("exchange_api_key_missing")

        if not request.checkbox_enabled:
            reasons.append("autotrade_checkbox_not_enabled")

        if not request.risk_guard_enabled:
            reasons.append("risk_guard_disabled")

        if request.kill_switch_active:
            reasons.append("kill_switch_active")

        allowed = len(reasons) == 0
        return {
            "ready": True,
            "allowed": allowed,
            "mode": "personal_only",
            "exchange": request.exchange,
            "execution_engine_loaded": False,
            "real_order_execution_enabled": False,
            "commercial_included": False,
            "reasons": reasons if reasons else ["autotrade_gate_passed_but_execution_engine_not_loaded"],
        }
