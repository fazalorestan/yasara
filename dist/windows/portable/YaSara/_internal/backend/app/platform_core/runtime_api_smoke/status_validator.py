class RuntimeAPIStatusValidator:
    def validate_status(self, status_code: int):
        return {"valid": status_code == 200, "status_code": status_code}

    def validate_payload(self, payload):
        if not isinstance(payload, dict):
            return {"valid": False, "reason": "payload_not_object"}
        if "detail" in payload and payload["detail"] == "Not Found":
            return {"valid": False, "reason": "not_found_payload"}
        if "ready" in payload and payload["ready"] is not True:
            return {"valid": False, "reason": "ready_not_true"}
        return {"valid": True, "reason": "ok"}

runtime_api_status_validator = RuntimeAPIStatusValidator()
