from pydantic import BaseModel, Field

class RuntimeSmokeCheckV1(BaseModel):
    name: str
    status: str = "pending"
    required: bool = True

class RuntimeSmokePlanV1(BaseModel):
    checks: list[RuntimeSmokeCheckV1] = Field(default_factory=list)

class RuntimeSmokePlannerV1:
    def build(self) -> RuntimeSmokePlanV1:
        return RuntimeSmokePlanV1(checks=[
            RuntimeSmokeCheckV1(name="backend_import"),
            RuntimeSmokeCheckV1(name="health_endpoint"),
            RuntimeSmokeCheckV1(name="swagger_docs"),
            RuntimeSmokeCheckV1(name="release_summary"),
        ])
