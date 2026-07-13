class APIResponseValidator:
    def validate_status(self, status_code: int):
        return {"valid": status_code == 200, "status_code": status_code}

    def validate_json(self, payload):
        return {"valid": isinstance(payload, (dict, list)), "type": type(payload).__name__}

    def validate_ready_field(self, payload):
        if isinstance(payload, dict) and "ready" in payload:
            return {"valid": payload.get("ready") is True, "has_ready": True}
        return {"valid": True, "has_ready": False}

api_response_validator = APIResponseValidator()
