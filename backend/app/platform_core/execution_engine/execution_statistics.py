class ExecutionStatisticsService:
    def statistics(self):
        return {
            "ready": True,
            "dry_run_ratio": 1.0,
            "real_execution_ratio": 0.0,
            "rejection_rate": 0.0,
            "audit_coverage": 1.0,
            "execution_allowed": False,
        }

execution_statistics_service = ExecutionStatisticsService()
