class IndicatorMathSafetyValidator:
    def validate_number(self, value):
        if value is None:
            return {"valid": True, "value": None}
        if isinstance(value, (int, float)) and value == value and value not in [float("inf"), float("-inf")]:
            return {"valid": True, "value": value}
        return {"valid": False, "error": "invalid_number"}

indicator_math_safety_validator = IndicatorMathSafetyValidator()
