from app.release_v1.domain.models import LoadTestPlan, LoadTestScenario

class LoadTestPlannerV1:
    def default_plan(self) -> LoadTestPlan:
        return LoadTestPlan(
            scenarios=[
                LoadTestScenario(name="health", users=25, duration_seconds=60, endpoint="/health"),
                LoadTestScenario(name="dashboard_snapshot", users=20, duration_seconds=120, endpoint="/api/v1/dashboard-v1/snapshot"),
                LoadTestScenario(name="mobile_home", users=20, duration_seconds=120, endpoint="/api/v1/mobile-v1/home"),
                LoadTestScenario(name="strategy_list", users=10, duration_seconds=90, endpoint="/api/v1/strategy-builder-v1/strategies"),
            ]
        )
