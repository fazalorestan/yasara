from pydantic import BaseModel, Field

class SmokeTestEndpointV1(BaseModel):
    name: str
    path: str
    expected_status: int = 200

class SmokeTestPlanV1(BaseModel):
    endpoints: list[SmokeTestEndpointV1] = Field(default_factory=list)

class SmokeTestPlannerV1:
    def build(self) -> SmokeTestPlanV1:
        return SmokeTestPlanV1(endpoints=[
            SmokeTestEndpointV1(name="health", path="/health"),
            SmokeTestEndpointV1(name="docs", path="/docs"),
            SmokeTestEndpointV1(name="release_summary", path="/api/v1/release-pro-v1/summary"),
            SmokeTestEndpointV1(name="consolidation_readiness", path="/api/v1/consolidation-v1/readiness"),
        ])
