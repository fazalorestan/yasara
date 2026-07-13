class RuntimeSignalValidator:
    def validate(self, signal: dict):
        errors = []
        direction = signal.get("direction")
        confidence = signal.get("confidence")
        if direction not in ["LONG", "SHORT", "WAIT"]:
            errors.append("invalid_direction")
        if not isinstance(confidence, int):
            errors.append("confidence_must_be_int")
        elif confidence < 0 or confidence > 100:
            errors.append("confidence_out_of_range")
        if signal.get("execution_allowed") is not False:
            errors.append("execution_must_remain_false")
        return {"valid": len(errors) == 0, "errors": errors}

runtime_signal_validator = RuntimeSignalValidator()
