class LiveDataSafetyPolicy:
    def policy(self):
        return {
            "ready": True,
            "read_only": True,
            "real_live_connection": False,
            "real_execution_enabled": False,
            "auto_trading_enabled": False,
            "requires_validation_before_publish": True,
            "execution_allowed": False,
        }

    def validate_snapshot(self, snapshot: dict):
        errors = []
        if not snapshot.get("source_id"):
            errors.append("missing_source_id")
        if not snapshot.get("symbol"):
            errors.append("missing_symbol")
        if float(snapshot.get("price", 0.0)) <= 0:
            errors.append("invalid_price")
        return {"ready": True, "valid": len(errors) == 0, "errors": errors}

live_data_safety_policy = LiveDataSafetyPolicy()
