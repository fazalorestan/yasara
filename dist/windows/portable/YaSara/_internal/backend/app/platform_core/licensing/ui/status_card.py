from app.platform_core.licensing.manager.status import license_status_reporter

class LicenseStatusCardContract:
    def build(self, payload: dict):
        status = license_status_reporter.status(payload)
        return {
            "ready": True,
            "title": "License Status",
            "license_type": status["license_type"],
            "features_count": status["features_count"],
            "expired": status["expired"],
            "valid_time": status["valid_time"],
            "badge": "Expired" if status["expired"] else status["license_type"].upper(),
            "execution_allowed": False,
        }

license_status_card_contract = LicenseStatusCardContract()
