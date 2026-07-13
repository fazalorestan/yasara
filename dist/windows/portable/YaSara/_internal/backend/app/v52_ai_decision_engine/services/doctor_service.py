class DoctorService:
    def health(self, dependencies: dict):
        checks = {k: {"ready": v is not None, "status": "ok" if v is not None else "unavailable"} for k, v in dependencies.items()}
        return {
            "ready": all(v["ready"] for v in checks.values()) if checks else False,
            "checks": checks,
            "signal_only_default": True,
            "auto_trading_enabled": False,
        }
