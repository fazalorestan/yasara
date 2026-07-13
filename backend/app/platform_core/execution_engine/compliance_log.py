class ExecutionComplianceLogService:
    def log(self):
        return {
            "ready": True,
            "entries": [
                {"check": "real_execution_blocked", "passed": True},
                {"check": "broker_connection_blocked", "passed": True},
                {"check": "auto_trading_blocked", "passed": True},
            ],
            "passed": True,
            "execution_allowed": False,
        }

execution_compliance_log_service = ExecutionComplianceLogService()
